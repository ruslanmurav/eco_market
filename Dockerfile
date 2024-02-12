FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Создаем директорию для приложения внутри контейнера
RUN mkdir /app

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы requirements.txt из вашего проекта в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости Python из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из вашего проекта в контейнер
COPY . /app/

# Запускаем Gunicorn приложение
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "eco_market.wsgi:application"]
