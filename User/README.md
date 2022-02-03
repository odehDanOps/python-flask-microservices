## Setup Database:
- `CREATE USER 'microservices'@'localhost' IDENTIFIED BY 'dev_2022';`
- `CREATE DATABASE micro_user_dev;`
- `GRANT ALL PRIVILEGES ON micro_user_dev.* TO 'microservices'@'localhost';`

## Generate Secret
Execute the code in terminal:
`>>> import secrets`
`>>> secrets.token_urlsafe(16)`

## Migration
Create a migration repository `flask db init`
- Run migration `flask db migrate`
- Apply the migration `flask db upgrade`
