# TASK.md — Поточне завдання

> Перед заповненням прочитай `AGENTS_GLOBAL.md` та `AI_AGENT_CONTEXT.md`.
> Очищуй цей файл і пиши нове завдання перед кожною задачею.

---

## Metadata

| Поле       | Значення                                               |
|------------|--------------------------------------------------------|
| Проект     | Pick-to-Belt                                           |
| Тип        | Bug / Enhancement / New Feature / Refactor             |
| Пріоритет  | Low / Medium / High / Critical                         |
| Статус     | Todo / In Progress / Review / Done                     |
| Файл(и)    | routes.py / models.py / servo_controller.py / template |
| Складність | S / M / L / XL                                         |

---

## Мета

<!-- Одне речення: що треба зробити і навіщо -->

---

## Опис

<!-- Детальний опис завдання:
- Що зараз є (поточна поведінка)
- Що повинно бути (очікувана поведінка)
- Які файли/моделі/ендпоінти зачеплені
-->

---

## Скриншоти / Мокапи

<!-- Посилання на файли в images/ або опис UI -->

---

## Технічні вимоги

### Backend (`app/routes.py`, `app/models.py`)
- [ ] Flask Blueprint маршрут з правильним методом (GET / POST / PUT / DELETE)
- [ ] `db.session.commit()` після кожної зміни
- [ ] Фонові задачі — `threading.Thread(daemon=True)` з `app.app_context()`
- [ ] Перевірка унікальності `servo_channel` перед збереженням (якщо стосується)
- [ ] `secure_filename` для завантаження файлів (якщо стосується)
- [ ] Відповідь: `jsonify({...})` для API, `render_template(...)` для сторінок

### Servo (`app/servo_controller.py`)
- [ ] Перевірити поведінку в simulation mode
- [ ] Використовувати `release_one()` або `release_multiple()` (не прямі I2C виклики)

### Frontend (шаблон)
- [ ] Vanilla JS `fetch()` + `async/await`
- [ ] Чисті render-функції повертають HTML-рядок
- [ ] Помилки відображати користувачу (alert або inline)
- [ ] Мова UI: українська
- [ ] Кольори: дотримуватись палітри (#2563eb, #16a34a, #f59e0b, #dc2626)

### Дані
- [ ] Оновити `orders_test.json` якщо потрібні нові тестові дані

---

## Критерії прийняття (Acceptance Criteria)

- [ ] ...
- [ ] ...
- [ ] Протестовано вручну (або в simulation mode)
- [ ] Не зламано існуючий функціонал (operator / admin / report)

---

## Definition of Done

- [ ] Всі acceptance criteria виконані
- [ ] Simulation mode працює коректно
- [ ] Перевірено в Docker (або локально)
- [ ] Коміт за Conventional Commits: `feat/fix/refactor(scope): description`
