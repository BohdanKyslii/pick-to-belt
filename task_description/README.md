# Task Description — Pick-to-Belt

Каталог з документацією та завданнями для розробки проекту **Pick-to-Belt**.

---

## Структура файлів

```
task_description/
├── AGENTS_GLOBAL.md      # ⭐ ГЛОБАЛЬНІ ПРАВИЛА (читати першим!)
├── AI_AGENT_CONTEXT.md   # Технічний контекст (моделі, API, серво, UI-патерни)
├── CLAUDE.md             # Швидкий довідник для Claude Code
├── TASK.md               # ← СЮДИ ПИШЕМО ПОТОЧНЕ ЗАВДАННЯ
├── CHANGES.md            # Журнал змін документації
├── README.md             # Цей файл
├── images/               # Скриншоти та мокапи до завдань
└── task_description/     # Шаблони для типових задач
    └── servo_test.md     # Шаблон: тестування серво-каналу
```

---

## Порядок читання

```
1. AGENTS_GLOBAL.md     — архітектура, бізнес-логіка, патерни, API
2. TASK.md              — конкретне завдання
3. AI_AGENT_CONTEXT.md  — технічні деталі моделей, функцій, UI
4. CLAUDE.md            — швидкий довідник з прикладами коду
5. images/              — скриншоти (якщо є)
```

---

## Як використовувати TASK.md

`TASK.md` — файл **поточного завдання**. Перед початком роботи:

1. Очисти старий зміст `TASK.md`
2. Заповни за шаблоном (метадані, мета, опис, технічні вимоги)
3. Додай скриншоти або мокапи в `images/` якщо потрібно

### Для Claude Code

Передай контекст у промпті:
```
Прочитай task_description/AGENTS_GLOBAL.md, task_description/TASK.md
та task_description/AI_AGENT_CONTEXT.md і виконай завдання.
```

Або просто відкрий проект у Claude Code — `CLAUDE.md` завантажується автоматично як системний контекст.

---

## Проект Pick-to-Belt — коротко

**Flask 3.x + SQLAlchemy + SQLite + smbus2 (I2C)**

| Файл                    | Що робить                                           |
|-------------------------|-----------------------------------------------------|
| `app/routes.py`         | Всі маршрути (сторінки + API Blueprint)             |
| `app/models.py`         | Product, Box, Order, OrderItem, StockLog            |
| `app/servo_controller.py` | I2C/PCA9685 — release_one/release_multiple        |
| `app/templates/operator.html` | Комплектація замовлень в реальному часі     |
| `app/templates/admin.html`    | Налаштування 16 слотів та коробок           |
| `app/templates/report.html`   | Аналітика за обраний період                 |

**Ключові правила:**
- Flask Blueprint для всіх маршрутів
- Daemon thread для фонових серво-задач
- Vanilla JS `fetch()` без фреймворків
- `db.session.commit()` після кожної зміни
- Simulation mode якщо I2C недоступний

---

## Типові завдання

| Тип задачі                  | Що чіпати                                              |
|-----------------------------|--------------------------------------------------------|
| Новий API ендпоінт          | `routes.py` → новий `@bp.route`                        |
| Нове поле моделі            | `models.py` → видалити `pick_to_belt.db` → перезапуск  |
| Зміна UI оператора          | `templates/operator.html` → JS + HTML                  |
| Нова статистика в звіті     | `routes.py::get_report()` + `templates/report.html`    |
| Зміна серво-логіки          | `servo_controller.py` + перевірка simulation mode      |
| Новий тип замовлення        | `models.py` + `routes.py::_pick_order()` + шаблон      |
| Зміна бізнес-логіки пікінгу | `routes.py::_pick_order()` (daemon thread)             |
