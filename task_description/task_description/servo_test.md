# Шаблон задачі: Тестування серво-каналу

> Використовується коли потрібно перевірити або налагодити конкретний канал PCA9685.

---

## TASK.md — Приклад заповнення

```markdown
## Metadata

| Поле       | Значення                    |
|------------|-----------------------------|
| Тип        | Bug / Enhancement           |
| Пріоритет  | High                        |
| Файл(и)    | servo_controller.py         |
| Складність | S                           |

## Мета
Перевірити коректність спрацювання каналу N на платі 0x40.

## Опис
- Поточна поведінка: канал N не відкривається / відкривається неповністю
- Очікувана поведінка: сервопривод відкривається на OPEN_ANGLE=90°, утримується 0.6с, закривається
- Файли: app/servo_controller.py (release_one, _set_pwm)

## Технічні вимоги

### Servo
- [ ] Перевірити OPEN_ANGLE / CLOSE_ANGLE константи
- [ ] Перевірити HOLD_TIME (0.6с)
- [ ] Перевірити MIN_PULSE / MAX_PULSE (102 / 512)
- [ ] Протестувати release_one(0x40, N) напряму через python shell
- [ ] Перевірити simulation mode (повинен логувати без помилок)

## Критерії прийняття
- [ ] release_one(0x40, N) повертає True
- [ ] Товар фізично потрапляє в лоток
- [ ] Simulation mode не кидає виключень
```

---

## Корисні команди для налагодження

```python
# Запуск Python shell з контекстом Flask
from app import create_app
app = create_app()

# Тест одного каналу
from app import servo_controller as servo
servo.release_one(0x40, 5)   # board=0x40, channel=5

# Тест множинного спрацювання
servo.release_multiple(0x40, 5, 3)   # 3 рази з паузою 0.5с

# Перевірка режиму
print(servo.is_simulation())   # True / False

# Сканування I2C шини (в терміналі Raspberry Pi)
# i2cdetect -y 1
```

---

## Константи серво (довідково)

```python
OPEN_ANGLE  = 90    # кут відкриття
CLOSE_ANGLE = 0     # кут закриття
HOLD_TIME   = 0.6   # секунд утримання
MIN_PULSE   = 102   # 0° (500 мкс)
MAX_PULSE   = 512   # 180° (2500 мкс)
```

Формула розрахунку PWM-значення:
```python
pulse = int(MIN_PULSE + (MAX_PULSE - MIN_PULSE) * angle / 180)
```
