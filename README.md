

## Что внутри

 Аутентификация через токен (DRF TokenAuth)
 CRUD для постов (только свой пост)
 Комментарии к постам через /posts/{id}/comments/
 Гости видят только опубликованные посты
 Пагинация: посты — по 10, комментарии — по 5 (можно менять через ?page_size=N)
 Поиск и сортировка
 Автогенерация Swagger/ReDoc через drf-spectacular

## Запуск

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver