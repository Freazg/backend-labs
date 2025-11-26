# Backend Labs

## Варіант лабораторної роботи 3

**Група:** IO-31  
**Номер варіанту:** 1 (31 % 3 = 1)  
**Функціонал:** Валюти

### Опис варіанту:
- Додано сутність **Currency** (валюта) з полями: id, code (USD/EUR/UAH), name
- У моделі **User** додано поле `default_currency_id` - валюта користувача за замовчуванням
- При створенні **Record** можна вказати `currency_id` (опціонально)
- Якщо `currency_id` не вказано, використовується валюта користувача за замовчуванням

---


Flask REST API для лабораторних робіт з курсу "Технології розроблення серверного програмного забезпечення"

## Вимоги

- Python 3.11+
- Docker (опціонально)

## Локальний запуск

### Використовуючи Python

1. Клонуйте репозиторій:
```bash
git clone <your-repo-url>
cd backend-labs
```

2. Створіть віртуальне середовище:
```bash
python3 -m venv env
source ./env/bin/activate  # Linux/Mac
# або env\Scripts\activate  # Windows
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

4. Запустіть застосунок:
```bash
python run.py
```

Застосунок буде доступний за адресою: http://localhost:5000

### Використовуючи Docker

1. Зберіть Docker image:
```bash
docker build . -t backend-labs:latest
```

2. Запустіть контейнер:
```bash
docker run -it --rm --network=host -e PORT=8080 backend-labs:latest
```

Застосунок буде доступний за адресою: http://localhost:8080

## API Endpoints

### GET /healthcheck

Перевірка стану сервісу

**Відповідь:**
```json
{
  "status": "OK",
  "date": "2025-11-24T19:23:19.916201"
}
```

## Деплой

Застосунок задеплоєний на Render.com: https://backend-labs-lm1i.onrender.com

## Lab 2: REST API для обліку витрат

### Структура API

API підтримує три основні сутності:
- **Users** - користувачі системи
- **Categories** - категорії витрат
- **Records** - записи про витрати

### Endpoints

#### Users
- `POST /user` - створення користувача
- `GET /users` - отримання всіх користувачів
- `GET /user/<user_id>` - отримання користувача за ID
- `DELETE /user/<user_id>` - видалення користувача

#### Categories
- `POST /category` - створення категорії
- `GET /category` - отримання всіх категорій
- `DELETE /category/<category_id>` - видалення категорії

#### Records
- `POST /record` - створення запису витрат
- `GET /record/<record_id>` - отримання запису за ID
- `GET /record?user_id=X` - фільтрація записів за користувачем
- `GET /record?category_id=X` - фільтрація записів за категорією
- `GET /record?user_id=X&category_id=Y` - фільтрація за обома параметрами
- `DELETE /record/<record_id>` - видалення запису

### Postman Testing

Колекція Postman з усіма запитами знаходиться в папці `postman/`:
- `Backend_Labs_Expense_Tracker.postman_collection.json` - колекція запитів
- `Local.postman_environment.json` - environment для локального тестування
- `Production.postman_environment.json` - environment для production

Для імпорту:
1. Відкрийте Postman
2. Collections → Import
3. Виберіть файл колекції
4. Environments → Import → виберіть environment файли
