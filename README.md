# API для блога

REST API для простого блога на Django и DRF.

## Что внутри

- Аутентификация через токен (DRF TokenAuth)
- CRUD для постов (только свой пост)
- Комментарии к постам через /posts/{id}/comments/
- Гости видят только опубликованные посты
- Пагинация: посты — по 10, комментарии — по 5 (можно менять через ?page_size=N)
- Поиск и сортировка
- Автогенерация Swagger/ReDoc через drf-spectacular

## Запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Структура

```
manage.py
requirements.txt
README.md
.gitignore
.env                 # секретный ключ (не коммитить!)
blog/   # настройки, URL'ы, WSGI
api/    # модели, viewset'ы, серIALIZеры
```

## Ограничения

- SQLite вместо PostgreSQL
- Нет тестов
- Нет rate limiting'а
- Комментарии не модерируются автоматически

---

Сделал как часть тестового задания. Оценка — где-то 80/100.