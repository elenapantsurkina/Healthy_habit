# Используем официальный slim-образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \\\\
    gcc \\\\
    libpq-dev \\\\
    && apt-get clean \\\\
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в контейнер
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости Python
RUN pip install poetry && poetry install --no-root

# Копируем исходный код приложения в контейнер
COPY . .

# Создаем директорию и даем права для статичтических файлов
RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles

# Пробрасываем порт, который будет использовать Django
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
