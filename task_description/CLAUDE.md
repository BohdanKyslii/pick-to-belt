# CLAUDE.md — Швидкий довідник для Claude Code

Контекст проекту для Claude Code. Перед кодом обов'язково читай `AGENTS_GLOBAL.md`.

---

## Проект

**Pick-to-Belt** — Flask система автоматизованого комплектування замовлень на конвеєр.

**Tech Stack:**
- Flask 3.x + Flask-SQLAlchemy (SQLite)
- Vanilla JS + HTML/CSS (без фреймворків)
- smbus2 — I2C керування PCA9685 (сервоприводи)
- Docker (ARM64) + GitHub Actions CI/CD

---

## Команди

```bash
# Локальний запуск
pip install -r requirements.txt
python run.py                    # http://localhost:5000

# Docker
docker compose up -d             # запуск
docker compose logs -f web       # логи
docker compose down              # зупинка
```

---

## Алгоритм роботи над завданням

1. Читай `AGENTS_GLOBAL.md` — архітектура, бізнес-логіка, патерни
2. Читай `TASK.md` — конкретне завдання
3. Читай `AI_AGENT_CONTEXT.md` — моделі, функції, UI-патерни
4. Переглянь `images/` — скриншоти або мокапи (якщо є)
5. Плануй → пиши → тестуй вручну

---

## Патерни (обов'язкові)

### Flask маршрут (JSON API)

```python
@bp.route("/api/orders/<int:order_db_id>/start", methods=["POST"])
def start_order(order_db_id):
    order = Order.query.get_or_404(order_db_id)
    data = request.get_json()
    order.box_id = data.get("box_id")
    order.status = "picking"
    order.started_at = datetime.utcnow()
    db.session.commit()
    thread = threading.Thread(target=_pick_order, args=(order_db_id,), daemon=True)
    thread.start()
    return jsonify({"status": "ok"})
```

### Flask маршрут (HTML сторінка)

```python
@bp.route("/")
def index():
    return render_template("operator.html")
```

### SQLAlchemy — додавання запису

```python
product = Product(articl="12345", name="Назва", servo_channel=0)
db.session.add(product)
db.session.commit()
```

### SQLAlchemy — оновлення

```python
product = Product.query.get_or_404(product_id)
product.name = data.get("name", product.name)
db.session.commit()
```

### Фонова задача (servo)

```python
def _pick_order(order_db_id):
    with app.app_context():
        # ... логіка комплектування
        db.session.commit()

thread = threading.Thread(target=_pick_order, args=(order_db_id,), daemon=True)
thread.start()
```

### Frontend — fetch API

```javascript
async function startOrder(orderId) {
    const boxId = document.getElementById(`box-${orderId}`).value;
    const res = await fetch(`/api/orders/${orderId}/start`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ box_id: parseInt(boxId) })
    });
    if (res.ok) {
        await loadOrders();
    }
}
```

### Frontend — рендер HTML

```javascript
function renderItem(item) {
    return `
        <div class="item-card" data-status="${item.status}">
            <img src="/static/uploads/${item.photo}" width="52">
            <span>${item.name} (${item.articl})</span>
            <span>${item.quantity_ordered} шт.</span>
        </div>
    `;
}
```

---

## Структура файлів

```
app/__init__.py          → create_app(), db.init_app(), db.create_all()
app/models.py            → Product, Box, Order, OrderItem, StockLog
app/routes.py            → bp = Blueprint("main"); всі маршрути
app/servo_controller.py  → release_one(), release_multiple(), is_simulation()
app/templates/           → operator.html, admin.html, report.html
static/uploads/          → фото товарів (збережені через secure_filename)
data/orders_test.json    → тестові замовлення для завантаження
```

---

## Важливо

- Фонові задачі (servo) — **тільки daemon thread** з `app.app_context()`
- `db.session.commit()` — після **кожної** зміни даних
- Унікальність `servo_channel` — перевіряти в маршруті, не в моделі
- Фото — завжди `secure_filename()` перед збереженням
- UI мова — **українська**
- Simulation mode — перевіряти через `servo_controller.is_simulation()`
- Нові ендпоінти — реєструвати в Blueprint `bp` у `app/routes.py`
