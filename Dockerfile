FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /app

# Run migrations and start app
CMD flask --app run db upgrade && gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"
