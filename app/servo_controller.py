"""
Керування серводвигунами через PCA9685.
На реальному Pi використовує smbus2.
В режимі розробки (без Pi) — симулює роботу.
"""
import time
import logging

logger = logging.getLogger(__name__)

OPEN_ANGLE = 90     # кут відкриття засувки
CLOSE_ANGLE = 0     # кут закриття
HOLD_TIME = 0.6     # секунд тримати відкритим
MIN_PULSE = 102     # ~500мкс = 0°
MAX_PULSE = 512     # ~2500мкс = 180°

_bus = None
_initialized = False
_simulation_mode = False


def _init_bus():
    """Ініціалізація I2C шини і PCA9685."""
    global _bus, _initialized, _simulation_mode
    if _initialized:
        return

    try:
        import smbus2
        _bus = smbus2.SMBus(1)
        _initialized = True
        _simulation_mode = False
        logger.info("PCA9685 ініціалізовано на I2C шині 1")
    except Exception as e:
        logger.warning(f"Не вдалось ініціалізувати I2C: {e}. Режим симуляції.")
        _simulation_mode = True
        _initialized = True


def _init_board(board_addr: int):
    """Ініціалізація конкретної плати PCA9685."""
    if _simulation_mode:
        return
    try:
        _bus.write_byte_data(board_addr, 0x00, 0x10)   # sleep
        time.sleep(0.05)
        _bus.write_byte_data(board_addr, 0xFE, 0x79)   # 50Hz
        time.sleep(0.05)
        _bus.write_byte_data(board_addr, 0x01, 0x04)   # MODE2 OUTDRV
        _bus.write_byte_data(board_addr, 0x00, 0x20)   # normal mode
        time.sleep(0.05)
    except Exception as e:
        logger.error(f"Помилка ініціалізації плати {hex(board_addr)}: {e}")


_boards_initialized = set()


def _ensure_board(board_addr: int):
    """Ініціалізуємо плату один раз."""
    _init_bus()
    if board_addr not in _boards_initialized:
        _init_board(board_addr)
        _boards_initialized.add(board_addr)


def _set_pwm(board_addr: int, channel: int, angle: float):
    """Встановити кут серво."""
    if _simulation_mode:
        logger.info(f"[SIM] board={hex(board_addr)} ch={channel} angle={angle}°")
        return

    pulse = int(MIN_PULSE + (angle / 180.0) * (MAX_PULSE - MIN_PULSE))
    reg = 0x06 + 4 * channel
    try:
        _bus.write_byte_data(board_addr, reg, 0)
        _bus.write_byte_data(board_addr, reg + 1, 0)
        _bus.write_byte_data(board_addr, reg + 2, pulse & 0xFF)
        _bus.write_byte_data(board_addr, reg + 3, pulse >> 8)
    except Exception as e:
        logger.error(f"Помилка запису серво board={hex(board_addr)} ch={channel}: {e}")


def release_one(board_addr: int, channel: int) -> bool:
    """Відкрити засувку одного осередку і закрити назад."""
    _ensure_board(board_addr)
    try:
        logger.info(f"Відкриваємо board={hex(board_addr)} ch={channel}")
        _set_pwm(board_addr, channel, OPEN_ANGLE)
        time.sleep(HOLD_TIME)
        _set_pwm(board_addr, channel, CLOSE_ANGLE)
        time.sleep(0.3)
        return True
    except Exception as e:
        logger.error(f"Помилка release_one: {e}")
        return False


def release_multiple(board_addr: int, channel: int, count: int) -> bool:
    """Відкрити засувку кілька разів для count одиниць товару."""
    _ensure_board(board_addr)
    for i in range(count):
        success = release_one(board_addr, channel)
        if not success:
            return False
        if i < count - 1:
            time.sleep(0.5)
    return True


def is_simulation() -> bool:
    return _simulation_mode
