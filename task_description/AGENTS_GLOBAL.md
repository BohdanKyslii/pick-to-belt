# AGENTS_GLOBAL.md — Глобальні правила проекту Pick-to-Belt

Цей документ містить правила, стандарти та архітектурні рішення для проекту **Pick-to-Belt**.
Обов'язковий до ознайомлення перед будь-яким завданням.

---

## 1. Огляд проекту

**Pick-to-Belt** — система автоматизації складського комплектування замовлень.

Фізичні лотки з товарами підключені до сервоприводів (PCA9685 I2C). Оператор запускає замовлення, система автоматично відкриває потрібні лотки на конвеєрну стрічку. Позиції без серво-прив'язки або з нульовим залишком підтверджуються оператором вручну.

**Три інтерфейси:**

| Сторінка  | URL       | Призначення                                      |
|-----------|-----------|--------------------------------------------------|
| Operator  | `/`       | Комплектація замовлень в реальному часі          |
| Admin     | `/admin`  | Налаштування 16 товарних слотів та коробок       |
| Report    | `/report` | Аналітика відвантажень за обраний період         |

**Користувачі:** оператор складу (одна роль, без авторизації).

---

## 2. Tech Stack

| Компонент      | Технологія                                     |
|----------------|------------------------------------------------|
| Backend        | Flask 3.x + Flask-SQLAlchemy 3.x               |
| Database       | SQLite (`data/pick_to_belt.db`)                |
| Frontend       | Vanilla JS + HTML/CSS (без фреймворків)        |
| Hardware       | PCA9685 I2C PWM driver (smbus2)                |
| Контейнеризація | Docker (ARM64 / Raspberry Pi)                 |
| CI/CD          | GitHub Actions → ghcr.io → self-hosted runner  |
| Python         | 3.11+                                          |

---

## 3. Структура проекту

```
pick-to-belt/
├── app/
│   ├── __init__.py            # Flask application factory
│   ├── models.py              # SQLAlchemy моделі
│   ├── routes.py              # Blueprint: сторінки + API ендпоінти
│   ├── servo_controller.py    # I2C/PCA9685 управління
│   └── templates/
│       ├── operator.html      # Інтерфейс оператора
│       ├── admin.html         # Адміністрування
│       └── report.html        # Звіти
├── data/
│   ├── pick_to_belt.db        # SQLite (авто-генерується)
│   └── orders_test.json       # Тестові замовлення
├── static/
│   └── uploads/               # Фото товарів
├── docs/                      # Документація проекту
├── task_description/          # Завдання для розробника / AI
├── run.py                     # Точка входу (порт 5000)
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 4. Моделі даних

### Product
Товар, прив'язаний до серво-лотка.
- `articl` (unique) — артикул
- `servo_board` / `servo_channel` — адреса PCA9685 + канал (0–15)
- `cell_capacity` / `cell_stock` — ємність та поточний залишок
- `sticker_count` / `sticker_note` — стікери при пакуванні
- `comment` — інструкція оператору
- `photo` — шлях до фото
- `is_active`, `created_at`, `updated_at`

### Box
Тип пакувальної коробки.
- `name` — маркування (напр. `"M - 30×40×20"`)
- `length` / `width` / `height` — розміри, мм
- `is_active`

### Order
Замовлення на комплектацію.
- `order_id` (unique) — зовнішній номер
- `status`: `pending` → `picking` → `packed` → `done`
- `box_id` FK→Box
- `created_at`, `started_at`, `packed_at`

### OrderItem
Позиція в замовленні.
- `articl` — артикул товару
- `quantity_ordered` / `quantity_picked`
- `is_manual` — потребує ручного збору
- `status`: `pending` → `picking` → `done` / `manual` / `partial`

### StockLog
Лог списань залишків (аудит).
- `articl`, `order_id`, `quantity`, `created_at`

---

## 5. API структура

**Базовий префікс:** `/api`

| Endpoint                             | Метод | Дія                                    |
|--------------------------------------|-------|----------------------------------------|
| `/api/orders`                        | GET   | Список pending/picking замовлень       |
| `/api/orders/load`                   | POST  | Завантажити з orders_test.json         |
| `/api/orders/<id>/start`             | POST  | Запустити комплектацію                 |
| `/api/orders/<id>/confirm_manual`    | POST  | Підтвердити ручні позиції              |
| `/api/orders/<id>/packed`            | POST  | Позначити як запаковане                |
| `/api/orders/<id>/done`              | POST  | Завершити замовлення                   |
| `/api/products`                      | GET   | Список товарів                         |
| `/api/products`                      | POST  | Створити товар                         |
| `/api/products/<id>`                 | PUT   | Оновити товар                          |
| `/api/products/<id>/photo`           | POST  | Завантажити фото                       |
| `/api/products/init_16`              | POST  | Ініціалізувати 16 тестових товарів     |
| `/api/boxes`                         | GET   | Список коробок                         |
| `/api/boxes`                         | POST  | Створити коробку                       |
| `/api/boxes/init`                    | POST  | Ініціалізувати стандартні коробки      |
| `/api/report`                        | GET   | Аналітика (`?days=7`)                  |

---

## 6. Стиль коду

### Python (Backend)
- Flask Blueprint для всіх маршрутів
- `db.session.commit()` після кожної зміни стану
- Фонові операції (servo picking) — daemon thread через `threading.Thread`
- Логування помилок через `print()` (без окремого logger)
- Перевірка унікальності `servo_channel` на рівні маршруту (не на рівні моделі)
- Фото — тільки `werkzeug.utils.secure_filename` перед збереженням

### JavaScript (Frontend)
- Ніяких фреймворків (no React, no Vue, no jQuery)
- `fetch()` + `async/await` для всіх API запитів
- `renderOrder()` / `renderItem()` — чисті функції, повертають HTML-рядок
- `init()` — точка входу при завантаженні сторінки

### HTML/CSS
- Всі стилі — inline `<style>` у шаблоні
- Мова UI: **українська**
- Кольорова палітра:
  - Синій `#2563eb` — primary дії
  - Зелений `#16a34a` — success / done
  - Жовтий `#f59e0b` — warning / partial
  - Червоний `#dc2626` — danger / manual
  - Сірий `#6b7280` — neutral

---

## 7. Бізнес-логіка комплектування

```
_pick_order(order_id):
  для кожного OrderItem:
    item.status = 'picking'
    product = знайти за articl
    якщо не знайдено → status='manual', is_manual=True
    якщо stock == 0 → status='manual'
    якщо stock >= qty → servo.release_multiple(); списати stock; status='done'
    якщо 0 < stock < qty → servo.release_multiple(stock); status='partial'
    записати StockLog
    db.session.commit()
```

Оператор підтверджує `manual`/`partial` через кнопку → `confirm_manual` API.

---

## 8. Серво-контролер

| Константа    | Значення | Опис                          |
|--------------|----------|-------------------------------|
| OPEN_ANGLE   | 90       | Кут відкриття лотка           |
| CLOSE_ANGLE  | 0        | Кут закриття                  |
| HOLD_TIME    | 0.6 с    | Час утримання у відкритому    |
| MIN_PULSE    | 102      | ~500 мкс → 0°                 |
| MAX_PULSE    | 512      | ~2500 мкс → 180°              |

Якщо smbus2 недоступний — автоматичний **simulation mode** (логи без hardware).

---

## 9. Git Workflow

**Гілки:**
- `feature/short-name` — нова функціональність
- `bugfix/issue-name` — виправлення

**Коміти (Conventional Commits):**
```
feat(routes): add order export endpoint
fix(servo): correct hold time for channel 5
refactor(models): add index on order status
docs: update task description files
```

---

## 10. Безпека та конфігурація

- `SECRET_KEY` — через змінну середовища (docker-compose.yml або .env)
- Фото: перевірка розширення (`png`, `jpg`, `jpeg`, `gif`, `webp`) + `secure_filename`
- Максимальний розмір файлу: 16 МБ (`MAX_CONTENT_LENGTH`)
- I2C пристрій: `/dev/i2c-1` (монтується як device у Docker)
