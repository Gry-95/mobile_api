## API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.

## Запуск приложения
```bash
docker-compose up --build
```


### Рализованы запросы

#### GET - получить список Торговых точек привязанных к переданному номеру телефона

```
/api/shops/
```

#### POST - выполнить посещение в Торговую точку

```
/api/visits/
```

#### CURL для теста

```bash
curl --location 'http://127.0.0.1:8000/api/shops/' \
--header 'Authorization: Phone +1234567890' \
--data ''
```

```bash
curl --location 'http://127.0.0.1:8000/api/visits/' \
--header 'Authorization: Phone +1234567890' \
--header 'Content-Type: application/json' \
--data '{
    "shop_pk": 1,
    "latitude": 56.7558,
    "longitude": 38.6176
}'
```