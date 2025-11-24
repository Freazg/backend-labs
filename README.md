# Backend Labs

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
