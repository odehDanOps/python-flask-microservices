## Setup Database:
```
CREATE USER 'microservices'@'localhost' IDENTIFIED BY 'dev_2022';
CREATE DATABASE micro_user_dev;
GRANT ALL PRIVILEGES ON micro_user_dev.* TO 'microservices'@'localhost';
```

## Generate Secret
Execute the code in terminal:
```
>>> import secrets
>>> secrets.token_urlsafe(16)
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
docker network create --driver bridge micro_network (skip if already created)
docker build -t user-srv .
docker run -p 5001:5001 --detach --name user-service --net=micro_network user-srv
```

## Using 'flask shell' to access flask application
```
$ flask shell
from application.models import User
from application import db
admin = User(username="foo", email="foo@admin.com",first_name="foo", last_name="bar", password="admin2020",is_admin=True)
db.session.add(admin)
db.session.commit()
