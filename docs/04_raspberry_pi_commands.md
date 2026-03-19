# Raspberry Pi — Команди для роботи з Pick-to-Belt

## Підключення до Pi

```bash
# SSH підключення
ssh rasberry_kisliy@pi-kisliy

# або за IP-адресою
ssh rasberry_kisliy@192.168.x.x
```

---

## Git — синхронізація коду

```bash
# Перейти в директорію проекту
cd ~/pick-to-belt

# Підтягнути останні зміни з GitHub
git pull

# Перевірити статус
git status

# Переглянути останні коміти
git log --oneline -10

# Примусово оновити до стану remote (скидає локальні зміни)
git fetch origin
git reset --hard origin/main
```

---

## Docker — основні команди

### Запуск

```bash
# Запустити контейнери у фоновому режимі
docker compose up -d

# Запустити та відразу переглядати логи
docker compose up
```

### Зупинка

```bash
# Зупинити контейнери (дані зберігаються)
docker compose stop

# Зупинити та видалити контейнери і мережі (дані зберігаються)
docker compose down

# Зупинити та видалити все включно з volumes (⚠️ дані БД будуть видалені!)
docker compose down -v
```

### Перезапуск

```bash
# Перезапустити всі сервіси
docker compose restart

# Перезапустити тільки web-сервіс
docker compose restart web
```

### Збірка образу

```bash
# Зібрати образ з Dockerfile (при зміні коду або requirements.txt)
docker compose build

# Зібрати без кешу (чиста збірка)
docker compose build --no-cache

# Зібрати та одразу запустити
docker compose up -d --build
```

### Оновлення після git pull

```bash
# Стандартний цикл оновлення
git pull
docker compose down
docker compose build
docker compose up -d
```

---

## Логи

```bash
# Переглянути логи (останні 100 рядків)
docker compose logs --tail=100

# Логи в реальному часі (слідкувати)
docker compose logs -f

# Логи тільки web-сервісу
docker compose logs -f web

# Логи з позначкою часу
docker compose logs -f -t web
```

---

## Виконання команд всередині контейнера

```bash
# Відкрити bash всередині контейнера
docker compose exec web bash

# Перевірити встановлені пакети
docker compose exec web pip list

# Перевірити конкретний пакет
docker compose exec web pip show openpyxl

# Запустити Python shell Flask
docker compose exec web python -c "from app import create_app; app = create_app(); app.app_context().push()"

# Перевірити версію Python
docker compose exec web python --version
```

---

## База даних SQLite

```bash
# Відкрити SQLite консоль
docker compose exec web sqlite3 /app/data/pick_to_belt.db

# Корисні SQLite команди (всередині консолі):
# .tables                    — список таблиць
# .schema products           — структура таблиці
# SELECT * FROM orders;      — переглянути замовлення
# SELECT * FROM products;    — переглянути товари
# .quit                      — вийти

# Зробити резервну копію БД (на хості Pi)
cp ~/pick-to-belt/data/pick_to_belt.db ~/pick-to-belt/data/pick_to_belt_backup_$(date +%Y%m%d).db
```

---

## I2C / Hardware

```bash
# Сканувати I2C шину (знайти PCA9685 за адресою 0x40)
i2cdetect -y 1

# Перевірити чи є доступ до I2C всередині контейнера
docker compose exec web python -c "import smbus2; bus = smbus2.SMBus(1); print('I2C OK')"

# Перевірити режим роботи (simulation або hardware)
curl http://localhost:5000/api/status
```

---

## Моніторинг ресурсів

```bash
# Переглянути запущені контейнери та їх статус
docker compose ps

# Статистика використання ресурсів (CPU, RAM)
docker stats

# Статистика тільки pick-to-belt
docker stats pick-to-belt-web-1

# Переглянути всі образи
docker images

# Переглянути зайнятий простір Docker
docker system df
```

---

## Очищення

```bash
# Видалити зупинені контейнери, невикористані образи та мережі
docker system prune

# Видалити тільки невикористані образи
docker image prune

# Видалити конкретний старий образ
docker rmi <image_id>
```

---

## Типовий workflow після змін в коді

```bash
# 1. На Windows — закомітити та запушити
git add --renormalize -A
git commit -m "feat: опис змін"
git push

# 2. На Raspberry Pi — підтягнути та перезапустити
cd ~/pick-to-belt
git pull
docker compose up -d --build

# 3. Перевірити логи
docker compose logs -f web
```

---

## Налаштування git на Pi (перший раз)

```bash
cd ~/pick-to-belt

# Якщо репо ще не ініціалізовано
git init
git remote add origin https://github.com/bohdankyslii/pick-to-belt.git
git fetch origin
git checkout -b main --track origin/main

# Налаштувати LF для закінчень рядків
git config core.autocrlf false
```

---

## Корисні адреси (при підключенні до тієї ж мережі)

| Сторінка        | URL                          |
|-----------------|------------------------------|
| Оператор        | `http://pi-kisliy:5000/`     |
| Налаштування    | `http://pi-kisliy:5000/admin`|
| Звіт            | `http://pi-kisliy:5000/report`|
| API статус      | `http://pi-kisliy:5000/api/status` |
