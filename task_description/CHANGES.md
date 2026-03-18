# CHANGES.md — Журнал змін документації

---

## 2026-03-18 — Повна переробка під проект Pick-to-Belt

### Причина
Всі файли `task_description/` були скопійовані з попереднього проекту (Expenses/Django)
і не відповідали реальному проекту Pick-to-Belt (Flask).

### Що змінено

#### AGENTS_GLOBAL.md
- Повністю переписано під Pick-to-Belt
- Замінено: Django → Flask, PostgreSQL → SQLite, Bootstrap → Vanilla JS
- Видалено: CBV, ModelForm, crispy-forms, migrations, ruff, pre-commit
- Додано: опис 5 моделей (Product, Box, Order, OrderItem, StockLog)
- Додано: повна таблиця API ендпоінтів
- Додано: бізнес-логіка комплектування (`_pick_order`)
- Додано: опис серво-контролера (константи, simulation mode)
- Оновлено: Git workflow та команди розробки

#### AI_AGENT_CONTEXT.md
- Повністю переписано
- Додано: реальна конфігурація Flask (`__init__.py`)
- Додано: повні визначення моделей з типами полів
- Додано: сигнатури функцій серво-контролера з описом
- Додано: перелік JS-функцій для кожного шаблону
- Додано: формат JSON замовлень
- Додано: таблиця типових помилок
- Додано: Docker конфігурація

#### CLAUDE.md
- Повністю переписано
- Видалено: Django команди, CBV патерни, crispy-forms, ruff
- Додано: Flask маршрут (API + сторінка)
- Додано: SQLAlchemy патерни (додавання, оновлення)
- Додано: патерн фонової задачі з `app_context()`
- Додано: frontend патерни (fetch + render)
- Оновлено: список важливих правил

#### TASK.md
- Переписано як порожній шаблон для Pick-to-Belt
- Видалено: Django-специфічні чеклисти (CBV, migrations, crispy-forms)
- Замінено: нові чеклисти для Backend/Servo/Frontend/Дані
- Адаптовано: Definition of Done без ruff

#### README.md
- Повністю переписано
- Оновлено: структуру файлів (додано servo_test.md)
- Оновлено: таблицю файлів проекту
- Додано: таблицю типових завдань з прив'язкою до файлів

#### task_description/ruff_check.md → task_description/servo_test.md
- Замінено шаблон ruff (не використовується) на шаблон тестування серво-каналу
