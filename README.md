Для запуска: 

    docker-compose up
    python manage.py runserver
    python -m celery -A ccr_project worker 
    python -m celery -A ccr_project beat 

Эндпоинты:
    
127.0.0.1:8000/api/news/

    GET: Список News
    POST: Добавление News

Входные данные:
```json
{
        "title": "aaa",
        "text": "asd",
        "publication_date": "2023-03-31",
        "author": "adds",
        "image": "path/to/img"
}
```

Выходные данные:
```json
[
    {
        "id": 9,
        "title": "11",
        "text": "11",
        "publication_date": "2023-03-31",
        "author": "11",
        "image": "http://127.0.0.1:8000/media/news/2023-03-31/IMG_5928_W7iGQpC.jpg",
        "image_thumb": "http://127.0.0.1:8000/media/CACHE/images/news/2023-03-31/IMG_5928_W7iGQpC/497572bcd1e3c9010aa0664ee14a4458.png"
    },
    {
        "id": 10,
        "title": "aaa",
        "text": "asd",
        "publication_date": "2023-03-31",
        "author": "adds",
        "image": "http://127.0.0.1:8000/media/news/2023-03-31/IMG_5928.png",
        "image_thumb": "http://127.0.0.1:8000/media/CACHE/images/news/2023-03-31/IMG_5928/b09009b40f50468a786ffe971ae10539.png"
    }
]
```

127.0.0.1:8000/api/news/<int:pk>
    
    GET: Вывод News c id = pk
    PUT: Внесение изменений
    DELETE: Удаление
Выходные данные:
```json
{
    "id": 7,
    "title": "111",
    "text": "222",
    "publication_date": "2023-03-31",
    "author": "3333",
    "image": "http://127.0.0.1:8000/media/news/2023-03-31/IMG_20230204_163842.jpg",
    "image_thumb": "http://127.0.0.1:8000/media/CACHE/images/news/2023-03-31/IMG_20230204_163842/57b22d43f8c091b6d52da11653280d52.png"
}
```


127.0.0.1:8000/api/upload/remarkable_places/ - загрузка данных из файла
    
    POST:
    Поля:
    - File upload - файл с расширением `.xlsx` Пример файла находится в корне директории (test.xlsx)

