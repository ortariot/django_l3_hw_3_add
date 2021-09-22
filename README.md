# Работа с базой (отображение списка моделей)

## Реализация

- `books_view` - функция отображения списка книг релизована в `books/views.py` (
адрес: `/books/` )
- `books_of_date_view` - функция отображение списка книг за дату с пагинацией релизована в `books/views.py` (адрес: `/books/2021-01-02/`) 

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

- Команда для создания миграций приложения для базы данных

```bash
python manage.py migrate
```

- Команда для запуска приложения

```bash
python manage.py runserver
```

- Для загрузки начальных данных модели Book необходимо выполнить команду:

```bash
python manage.py loaddata fixtures/books.json
```
