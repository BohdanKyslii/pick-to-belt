# AI_AGENT_CONTEXT.md — Технічний контекст проекту Pick-to-Belt

Технічний контекст для AI-агентів. Читати після `AGENTS_GLOBAL.md`.

---

## Проект

**Назва:** Pick-to-Belt
**Тип:** Flask веб-додаток для автоматизації складського комплектування
**БД:** SQLite (`data/pick_to_belt.db`)
**Середовище:** Docker (ARM64, Raspberry Pi)
**Python:** 3.11+
**Flask:** 3.x

---

## Конфігурація

```python
# app/__init__.py
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/pick_to_belt.db"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "pick-to-belt-secret")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB
```

```yaml
# docker-compose.yml (змінні середовища)
environment:
  - SECRET_KEY=your-secret-key
```

---

## Залежності (`requirements.txt`)

```
flask>=3.0
flask-sqlalchemy>=3.1
smbus2>=0.4.3
werkzeug>=3.0
```

---

## Flask Blueprint

Всі маршрути зареєстровані в одному Blueprint:

```python
# app/routes.py
bp = Blueprint("main", __name__)

# app/__init__.py
app.register_blueprint(bp)
```

Немає namespace, немає app_name — всі URL без префіксу.

---

## Моделі (`app/models.py`)

### Product

```python
class Product(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    articl       = db.Column(db.String(50), unique=True, nullable=False)
    name         = db.Column(db.String(200))
    servo_board  = db.Column(db.Integer, default=0x40)   # I2C адреса PCA9685
    servo_channel= db.Column(db.Integer, nullable=False)  # 0-15
    length       = db.Column(db.Float)    # мм
    width        = db.Column(db.Float)    # мм
    height       = db.Column(db.Float)    # мм
    weight       = db.Column(db.Float)    # г
    cell_capacity= db.Column(db.Integer, default=10)
    cell_stock   = db.Column(db.Integer, default=0)
    photo        = db.Column(db.String(300))   # відносний шлях
    sticker_count= db.Column(db.Integer, default=0)
    sticker_note = db.Column(db.String(300))
    comment      = db.Column(db.Text)
    is_active    = db.Column(db.Boolean, default=True)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self): ...  # servo_board як hex-рядок "0x40"
```

### Box

```python
class Box(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(100))
    length   = db.Column(db.Float)
    width    = db.Column(db.Float)
    height   = db.Column(db.Float)
    is_active= db.Column(db.Boolean, default=True)
    orders   = db.relationship("Order", backref="box")

    def to_dict(self): ...
```

### Order

```python
class Order(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    order_id   = db.Column(db.String(50), unique=True)
    status     = db.Column(db.String(20))  # pending/picking/packed/done
    box_id     = db.Column(db.Integer, db.ForeignKey("box.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime)
    packed_at  = db.Column(db.DateTime)
    items      = db.relationship("OrderItem", backref="order", cascade="all, delete-orphan")

    def to_dict(self): ...  # вкладені box + items[]
```

### OrderItem

```python
class OrderItem(db.Model):
    id               = db.Column(db.Integer, primary_key=True)
    order_db_id      = db.Column(db.Integer, db.ForeignKey("order.id"))
    articl           = db.Column(db.String(50))
    quantity_ordered = db.Column(db.Integer)
    quantity_picked  = db.Column(db.Integer, default=0)
    is_manual        = db.Column(db.Boolean, default=False)
    status           = db.Column(db.String(20))  # pending/picking/done/manual/partial

    def to_dict(self): ...  # підтягує name, stock, sticker_*, comment, photo з Product
```

### StockLog

```python
class StockLog(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    articl     = db.Column(db.String(50))
    order_id   = db.Column(db.String(50))
    quantity   = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

---

## Серво-контролер (`app/servo_controller.py`)

### Ключові функції

```python
release_one(board_addr: int, channel: int) -> bool
    # Відкрити → затримати HOLD_TIME → закрити
    # Повертає True при успіху, False при помилці
    # В simulation mode: логує і повертає True

release_multiple(board_addr: int, channel: int, count: int) -> None
    # Повторює release_one count разів з паузою 0.5с між спрацюваннями

is_simulation() -> bool
    # True якщо smbus2 недоступний або I2C недоступний
```

### PCA9685 регістри (довідково)

```python
MODE1    = 0x00
PRESCALE = 0xFE
LED0_ON_L = 0x06
# Частота: 50 Гц (PRESCALE = 121)
# Імпульс: MIN_PULSE=102 (0°) ... MAX_PULSE=512 (180°)
```

---

## Шаблони та UI

### Структура

```
app/templates/
├── operator.html   # 411 рядків — основна робоча сторінка
├── admin.html      # 393 рядки — налаштування товарів/коробок
└── report.html     # 100 рядків — аналітика
```

### Спільні UI-патерни у всіх шаблонах

- Sticky header з навігацією (`/`, `/admin`, `/report`)
- Значок `SIMULATION` якщо `is_simulation() == True`
- `fetch()` + `async/await` — всі запити до API
- Помилки відображаються через `alert()` або inline повідомлення
- Стан — тільки в DOM (без state management)

### operator.html — JavaScript функції

```javascript
init()              // Завантажити коробки, замовлення, перевірити simulation
loadOrders()        // GET /api/orders → renderOrder()
loadFromJson()      // POST /api/orders/load
startOrder(id)      // POST /api/orders/<id>/start з вибраним box_id
confirmManual(id)   // POST /api/orders/<id>/confirm_manual
packOrder(id)       // POST /api/orders/<id>/packed
renderOrder(order)  // Повертає HTML-рядок картки замовлення
renderItem(item)    // Повертає HTML-рядок позиції
```

### admin.html — JavaScript функції

```javascript
loadProducts()          // GET /api/products → renderCells()
loadBoxes()             // GET /api/boxes → renderBoxList()
openProductModal(ch)    // Відкрити модалку для каналу ch
saveProduct()           // POST/PUT + upload photo
saveBox()               // POST /api/boxes
initProducts()          // POST /api/products/init_16
initBoxes()             // POST /api/boxes/init
renderCells()           // Перемалювати сітку 4×4
renderCell(ch, prod)    // HTML комірки з індикатором залишку
```

### report.html — JavaScript функції

```javascript
loadReport()    // GET /api/report?days=N → заповнити KPI + top list
```

---

## Формат JSON замовлень (`data/orders_test.json`)

```json
[
  {
    "order_id": "РБН00010210",
    "items": [
      { "articl": "30770", "quantity": 1 },
      { "articl": "36403", "quantity": 2 }
    ]
  }
]
```

Якщо `articl` не знайдено в `Product` → позиція отримує `is_manual=True`, `status='manual'`.

---

## Типові помилки та як їх уникнути

| Неправильно | Правильно |
|-------------|-----------|
| `db.session.add()` без `commit()` | Завжди `db.session.commit()` після змін |
| `servo.release_one()` в основному потоці | Запускати через `threading.Thread(daemon=True)` |
| Прямий шлях до файлу фото | `secure_filename()` + перевірка розширення |
| `on_delete=CASCADE` для Product | Немає FK з Product → OrderItem (тільки `articl` рядком) |
| Перевірка унікальності каналу в моделі | Перевіряти в маршруті перед збереженням |
| `float` для фінансових розрахунків | Поки не використовується (тільки кількості та розміри) |

---

## Docker конфігурація

```yaml
# docker-compose.yml
services:
  web:
    image: ghcr.io/bohdankyslii/pick-to-belt:latest
    ports: ["5000:5000"]
    volumes:
      - ./data:/app/data
      - ./static/uploads:/app/static/uploads
    devices:
      - /dev/i2c-1:/dev/i2c-1
    environment:
      - SECRET_KEY=...
```

```dockerfile
# Dockerfile
FROM python:3.11-slim
RUN apt-get install -y i2c-tools
EXPOSE 5000
CMD ["python", "run.py"]
```

---

## CI/CD (`.github/workflows/deploy.yml`)

1. **Build:** Push до `main` → білд ARM64 образу → push до `ghcr.io`
2. **Deploy:** self-hosted runner → `docker compose up -d` на Raspberry Pi
