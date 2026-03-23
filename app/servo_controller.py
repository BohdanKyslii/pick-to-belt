"""
Керування серводвигунами через PCA9685.
На реальному Pi використовує smbus2.
В режимі розробки (без Pi) — симулює роботу.
"""
import time
import logging

logger = logging.getLogger(__name__)

OPEN_ANGLE = 90
CLOSE_ANGLE = 0
HOLD_TIME = 0.6
MIN_PULSE = 102
MAX_PULSE = 512

_bus = None
_simulation_mode = False
_boards_initialized = set()


def _get_bus():
    global _bus, _simulation_mode
    if _bus is not None:
        return _bus
    try:
        import smbus2
        _bus = smbus2.SMBus(1)
        _simulation_mode = False
        logger.info("smbus2 OK")
    except Exception as e:
        logger.warning(f"smbus2 failed: {e} — simulation mode")
        _simulation_mode = True
    return _bus


def _init_board(board_addr: int):
    bus = _get_bus()
    if _simulation_mode or bus is None:
        return
    try:
        bus.write_byte_data(board_addr, 0x00, 0x10)
        time.sleep(0.05)
        bus.write_byte_data(board_addr, 0xFE, 0x79)
        time.sleep(0.05)
        bus.write_byte_data(board_addr, 0x01, 0x04)
        bus.write_byte_data(board_addr, 0x00, 0x20)
        time.sleep(0.05)
        logger.info(f"Board {hex(board_addr)} initialized")
    except Exception as e:
        logger.error(f"Board init error {hex(board_addr)}: {e}")


def _ensure_board(board_addr: int):
    if board_addr not in _boards_initialized:
        _init_board(board_addr)
        _boards_initialized.add(board_addr)


def _set_pwm(board_addr: int, channel: int, angle: float):
    bus = _get_bus()
    if _simulation_mode or bus is None:
        logger.info(f"[SIM] board={hex(board_addr)} ch={channel} angle={angle}")
        return
    pulse = int(MIN_PULSE + (angle / 180.0) * (MAX_PULSE - MIN_PULSE))
    reg = 0x06 + 4 * channel
    try:
        bus.write_byte_data(board_addr, reg, 0)
        bus.write_byte_data(board_addr, reg + 1, 0)
        bus.write_byte_data(board_addr, reg + 2, pulse & 0xFF)
        bus.write_byte_data(board_addr, reg + 3, pulse >> 8)
    except Exception as e:
        logger.error(f"PWM write error: {e}")


def _disable_channel(board_addr: int, channel: int):
    """Повністю вимкнути PWM-сигнал на каналі (FULL_OFF bit).
    Запобігає жужжанню сервопривода після завершення руху.
    """
    bus = _get_bus()
    if _simulation_mode or bus is None:
        logger.info(f"[SIM] disable ch={channel}")
        return
    reg = 0x06 + 4 * channel
    try:
        bus.write_byte_data(board_addr, reg, 0x00)      # ON_L
        bus.write_byte_data(board_addr, reg + 1, 0x00)  # ON_H
        bus.write_byte_data(board_addr, reg + 2, 0x00)  # OFF_L
        bus.write_byte_data(board_addr, reg + 3, 0x10)  # OFF_H — FULL_OFF bit
    except Exception as e:
        logger.error(f"disable_channel error: {e}")


def set_angle(board_addr: int, channel: int, angle: float) -> bool:
    """Встановити кут серво і утримувати (без вимкнення PWM).
    Використовується для калібрування — серво тримає позицію.
    Щоб відпустити — викликати disable_channel().
    """
    _ensure_board(board_addr)
    try:
        _set_pwm(board_addr, channel, angle)
        logger.info(f"set_angle board={hex(board_addr)} ch={channel} angle={angle}")
        return True
    except Exception as e:
        logger.error(f"set_angle error: {e}")
        return False


def disable_channel(board_addr: int, channel: int) -> bool:
    """Вимкнути PWM на каналі — серво відпускається, не жужжить."""
    _ensure_board(board_addr)
    try:
        _disable_channel(board_addr, channel)
        return True
    except Exception as e:
        logger.error(f"disable_channel error: {e}")
        return False


def release_one(board_addr: int, channel: int,
                open_angle: float = OPEN_ANGLE,
                close_angle: float = CLOSE_ANGLE) -> bool:
    """Один цикл видачі: close_angle → open_angle → close_angle → disable.
    open_angle  — кут підйому механізму (налаштовується per-channel).
    close_angle — початкове/закрите положення (налаштовується per-channel).
    """
    _ensure_board(board_addr)
    try:
        _set_pwm(board_addr, channel, close_angle)
        time.sleep(0.15)
        _set_pwm(board_addr, channel, open_angle)
        time.sleep(HOLD_TIME)
        _set_pwm(board_addr, channel, close_angle)
        time.sleep(0.3)
        _disable_channel(board_addr, channel)
        return True
    except Exception as e:
        logger.error(f"release_one error: {e}")
        return False


def release_multiple(board_addr: int, channel: int, count: int,
                     open_angle: float = OPEN_ANGLE,
                     close_angle: float = CLOSE_ANGLE) -> bool:
    for i in range(count):
        if not release_one(board_addr, channel, open_angle, close_angle):
            return False
        if i < count - 1:
            time.sleep(0.5)
    return True


def is_simulation() -> bool:
    _get_bus()  # ініціалізуємо при першому виклику
    return _simulation_mode
