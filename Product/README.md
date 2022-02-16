## Setup Database:
```
CREATE USER 'microservices'@'localhost' IDENTIFIED BY 'dev_2022';
CREATE DATABASE micro_product_dev;
GRANT ALL PRIVILEGES ON micro_product_dev.* TO 'microservices'@'localhost';
```

## Migration
```
flask db init
flask db migrate -m '<message>'
flask db upgrade
```

## Running application in docker containers:
#### Using Docker CLI

```
docker network ls
docker network create --driver bridge micro_network (skip if already created)
docker build -t product-srv .
docker run -p 5002:5002 --detach --name product-service --net=micro_network product-srv
```

## Using 'flask shell' to access flask application
```
$ flask shell
from application.models import User
from application import db
admin = User(username="foo", email="foo@admin.com",first_name="foo", last_name="bar", password="admin2020",is_admin=True)
db.session.add(admin)
db.session.commit()
