FROM python:3.11-slim

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY devsecops-flask-app/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы
COPY /devsecops-flask-app/ .

# Открываем порт и запускаем Flask
EXPOSE 5000

CMD ["python", "app.py"]
