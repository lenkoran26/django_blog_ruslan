# Используем официальный образ python  в качестве базового
FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Устанавливаем рабочую директорию в контейнере
WORKDIR /code
# Копируем файл с зависимостями в рабочую директорию
COPY requirements.txt /code/
# устанавливаем зависимости
RUN pip install -r requirements.txt
# копируем все файлы проекта в контейнер
COPY . /code/
