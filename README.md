# edamap
Карта на которой собраны все харчевни с подробной информацией.

## Запуск проекта
```
git clone git@github.com:kikirilll/edamap.git
cd edamap
docker build -t <DOCKER_ACCOUNT>/edamap .
docker run -p 8000:8000 <DOCKER_ACCOUNT>/edamap
```

## Документация API
FastAPI собирает все доступные эндпоинты по адресу:
```
localhost:8000/docs
localhost:8000/redoc
```
Там же есть возможность сделать тестовые запросы.

## Структура БД
На данный момент БД состоит из одной таблицы `restaurants` с следующими колонками:
* `id` - id записи в БД (int)
* `name` - название заведения (string)
* `description` - некое описание (string)
* `image` - ссылка на картинку (string)
* `rating` - рейтинг (int)
* `lat` - широта (float)
* `lon` - долгота (float)

Для тестирования необходимо ручками предзаполнить данные в БД.