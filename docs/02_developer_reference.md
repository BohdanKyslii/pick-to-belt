# Pick-to-Belt — Довідник розробника

## Структура проекту

```
pick-to-belt/
├── app/
│   ├── __init__.py            # Flask application factory
│   ├── models.py              # SQLAlchemy моделі БД
│   ├── routes.py              # Всі маршрути (сторінки + API)
│   ├── servo_controller.py    # Управління I2C/PCA9685
│   └── templates/
│       ├── operator.html      # Інтерфейс оператора
│       ├── admin.html         # Адміністрування
│       └── report.html        # Звіти
├── data/
│   ├── pick_to_belt.db        # SQLite база (генерується автоматично)
│   └── orders_test.json       # Тестові замовлення
├── static/
│   └── uploads/               # Фото товарів
├── run.py                     # Точка входу
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Моделі даних (`app/models.py`)

### Product

Товар, прив'язаний до каналу сервопривода.

| Поле | Тип | Опис |
|------|-----|------|
| `id` | Integer PK | Автоінкремент |
| `articl` | String(50), unique, not null | Артикул товару |
| `name` | String(200), nullable | Назва товару |
| `servo_board` | Integer, default=0x40 | Адреса плати PCA9685 (I2C) |
| `servo_channel` | Integer, not null | Канал сервопривода (0–15) |
| `length` | Float, nullable | Довжина, мм |
| `width` | Float, nullable | Ширина, мм |
| `height` | Float, nullable | Висота, мм |
| `weight` | Float, nullable | Вага, г |
| `cell_capacity` | Integer, default=10 | Ємність лотка |
| `cell_stock` | Integer, default=0 | Поточний залишок |
| `photo` | String(300), nullable | Відносний шлях до фото |
| `sticker_count` | Integer, default=0 | Кількість стікерів |
| `sticker_note` | String(300), nullable | Опис стікера |
| `comment` | Text, nullable | Коментар для оператора |
| `is_active` | Boolean, default=True | Активний |
| `created_at` | DateTime, auto | Дата створення |
| `updated_at` | DateTime, auto | Дата оновлення |

**Методи:**
- `to_dict()` → `dict` — повертає всі поля; `servo_board` конвертується в hex-рядок (наприклад, `"0x40"`)

**Обмеження:** унікальність пари `(servo_board, servo_channel)` перевіряється на рівні маршрутів.

---

### Box

Тип пакувальної коробки.

| Поле | Тип | Опис |
|------|-----|------|
| `id` | Integer PK | Автоінкремент |
| `name` | String(100) | Назва/маркування (напр. `"A - 30×40×20"`) |
| `length` | Float, nullable | Довжина, мм |
| `width` | Float, nullable | Ширина, мм |
| `height` | Float, nullable | Висота, мм |
| `is_active` | Boolean, default=True | Активна |

**Методи:**
- `to_dict()` → `dict`

**Зв'язки:**
- `orders` ← `Order.box_id` (один-до-багатьох, через backref)

---

### Order

Замовлення на комплектацію.

| Поле | Тип | Опис |
|------|-----|------|
| `id` | Integer PK | Автоінкремент |
| `order_id` | String(50), unique | Зовнішній номер замовлення |
| `status` | String(20) | `pending` / `picking` / `packed` / `done` |
| `box_id` | Integer FK → Box | Обраний тип коробки |
| `created_at` | DateTime, auto | Створено |
| `started_at` | DateTime, nullable | Комплектація розпочата |
| `packed_at` | DateTime, nullable | Запаковано |

**Методи:**
- `to_dict()` → `dict` з вкладеними об'єктами `box` та `items[]`

**Зв'язки:**
- `box` → `Box` (багато-до-одного)
- `items` → `OrderItem[]` (один-до-багатьох, cascade delete-orphan)

---

### OrderItem

Позиція в замовленні.

| Поле | Тип | Опис |
|------|-----|------|
| `id` | Integer PK | Автоінкремент |
| `order_db_id` | Integer FK → Order | Замовлення |
| `articl` | String(50) | Артикул товару |
| `quantity_ordered` | Integer | Замовлена кількість |
| `quantity_picked` | Integer, default=0 | Автоматично зібрана кількість |
| `is_manual` | Boolean, default=False | Потребує ручного збору |
| `status` | String(20) | `pending` / `picking` / `done` / `manual` / `partial` |

**Методи:**
- `to_dict()` → `dict`; додатково підтягує з `Product`: `name`, `cell_stock`, `cell_capacity`, `sticker_count`, `sticker_note`, `comment`, `photo`

**Статусна логіка:**
```
pending → picking (при старті замовлення)
picking → done     (якщо зібрано всю кількість)
picking → partial  (якщо зібрано частину, залишок вручну)
picking → manual   (якщо товару немає в системі або залишок = 0)
manual/partial → done (після ручного підтвердження оператором)
```

---

### StockLog

Лог списань залишків.

| Поле | Тип | Опис |
|------|-----|------|
| `id` | Integer PK | Автоінкремент |
| `articl` | String(50) | Артикул |
| `order_id` | String(50) | Номер замовлення |
| `quantity` | Integer | Списана кількість |
| `created_at` | DateTime, auto | Час списання |

Немає методів, використовується виключно для запису.

---

## API маршрути (`app/routes.py`)

### Сторінки

| Маршрут | Метод | Шаблон |
|---------|-------|--------|
| `/` | GET | `operator.html` |
| `/admin` | GET | `admin.html` |
| `/report` | GET | `report.html` |

---

### Замовлення

#### `GET /api/orders`
Повертає замовлення зі статусами `pending` і `picking`.

**Відповідь:**
```json
{
  "orders": [ { ...order.to_dict() } ]
}
```

---

#### `POST /api/orders/load`
Завантажує замовлення з `data/orders_test.json`. Пропускає вже існуючі `order_id`.

**Формат JSON-файлу:**
```json
[
  {
    "order_id": "РБН00010210",
    "items": [
      { "articl": "30770", "quantity": 1 }
    ]
  }
]
```

**Відповідь:** `{ "loaded": N }`

---

#### `POST /api/orders/<id>/start`
Запускає комплектацію замовлення. Встановлює `status = picking`, обирає коробку, запускає `_pick_order()` у daemon-потоці.

**Тіло запиту:** `{ "box_id": 2 }`
**Відповідь:** `{ "status": "ok" }`

---

#### `POST /api/orders/<id>/confirm_manual`
Підтверджує ручне збирання всіх позицій зі статусами `manual` або `partial`. Встановлює їм `status = done`.

**Відповідь:** `{ "status": "ok" }`

---

#### `POST /api/orders/<id>/packed`
Позначає замовлення як запаковане. Встановлює `status = packed`, записує `packed_at`.

**Відповідь:** `{ "status": "ok" }`

---

#### `POST /api/orders/<id>/done`
Позначає замовлення як виконане (`status = done`).

**Відповідь:** `{ "status": "ok" }`

---

### Товари

#### `GET /api/products`
Повертає всі товари, відсортовані за `servo_channel`.

**Відповідь:** `{ "products": [ { ...product.to_dict() } ] }`

---

#### `POST /api/products`
Створює новий товар.

**Тіло запиту (JSON):**
```json
{
  "articl": "12345",
  "name": "Назва товару",
  "servo_channel": 0,
  "servo_board": "0x40",
  "cell_capacity": 10,
  "cell_stock": 5,
  "sticker_count": 2,
  "sticker_note": "Тип А",
  "comment": "Крихке"
}
```

**Валідація:** якщо канал `servo_channel` вже зайнятий на тій же платі → `400 Bad Request`.

---

#### `PUT /api/products/<id>`
Оновлює дані товару. Прийняті поля: `name`, `articl`, `servo_channel`, `servo_board`, `cell_capacity`, `cell_stock`, `sticker_count`, `sticker_note`, `comment`.

---

#### `POST /api/products/<id>/photo`
Завантаження фото товару. `multipart/form-data`, поле `photo`.

**Дозволені розширення:** `png`, `jpg`, `jpeg`, `gif`, `webp`
**Максимальний розмір:** 16 МБ
**Шлях збереження:** `static/uploads/<id>_<filename>`

---

#### `POST /api/products/init_16`
Створює 16 тестових товарів для каналів 0–15.

---

### Коробки

#### `GET /api/boxes`
Повертає активні коробки.

#### `POST /api/boxes`
Створює коробку. Поля: `name`, `length`, `width`, `height`.

#### `POST /api/boxes/init`
Ініціалізує 5 стандартних коробок: XS, S, M, L, XL.

---

### Звіти

#### `GET /api/report?days=7`
Аналітика за N днів (за замовчуванням 7).

**Відповідь:**
```json
{
  "total_orders": 15,
  "total_items": 48,
  "total_picked": 120,
  "manual_items": 6,
  "top_products": [
    { "articl": "30770", "name": "Товар А", "count": 45 }
  ]
}
```

---

## Модуль сервопривода (`app/servo_controller.py`)

### Константи

```python
OPEN_ANGLE  = 90    # Кут відкриття лотка
CLOSE_ANGLE = 0     # Кут закриття
HOLD_TIME   = 0.6   # Час утримання (секунди)
MIN_PULSE   = 102   # ~500 мкс → 0°
MAX_PULSE   = 512   # ~2500 мкс → 180°
```

### Функції

| Функція | Сигнатура | Опис |
|---------|-----------|------|
| `_init_bus()` | `() → None` | Ініціалізує I2C шину (`/dev/i2c-1`); при помилці → simulation mode |
| `_init_board(addr)` | `(int) → None` | Конфігурує PCA9685: 50 Гц PWM, MODE2 OUTDRV |
| `_ensure_board(addr)` | `(int) → None` | Lazy-ініціалізація плати при першому зверненні |
| `_set_pwm(addr, ch, angle)` | `(int, int, int) → None` | Встановлює кут сервопривода через I2C |
| `release_one(addr, ch)` | `(int, int) → bool` | Відкрити → затримати → закрити; повертає `True`/`False` |
| `release_multiple(addr, ch, count)` | `(int, int, int) → None` | Повторює `release_one` N разів з паузою 0.5 с |
| `is_simulation()` | `() → bool` | Чи активний режим симуляції |

### Режим симуляції

Активується автоматично якщо:
- `smbus2` не встановлений
- `/dev/i2c-1` недоступний
- Виникла помилка при ініціалізації шини

В режимі симуляції всі команди логуються через `print()`, але не передаються на hardware.

---

## Бізнес-логіка комплектування (`routes.py::_pick_order`)

```
Для кожного OrderItem у замовленні:
  1. item.status = 'picking'
  2. Пошук Product за articl
  3. Якщо не знайдено → item.is_manual = True, item.status = 'manual'
  4. Якщо stock == 0 → item.status = 'manual'
  5. Якщо stock >= quantity → servo.release_multiple(board, channel, quantity)
                              списати stock, item.status = 'done'
  6. Якщо 0 < stock < quantity → servo.release_multiple(board, channel, stock)
                                  списати stock, item.status = 'partial'
  7. Запис у StockLog
  8. db.session.commit()
```

---

## Flask Application Factory (`app/__init__.py`)

```python
def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/pick_to_belt.db"
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "pick-to-belt-secret")
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(bp)
    return app
```

---

## Змінні середовища

| Змінна | За замовчуванням | Опис |
|--------|-----------------|------|
| `SECRET_KEY` | `pick-to-belt-secret` | Flask secret key |

---

## Запуск локально

```bash
pip install -r requirements.txt
python run.py
# http://localhost:5000
```

## Запуск у Docker

```bash
docker compose up -d
```

Томи:
- `./data` → `/app/data` (SQLite)
- `./static/uploads` → `/app/static/uploads` (фото)
