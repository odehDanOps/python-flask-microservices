import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = "9Qj2adAU5iCuK45eWNcfeA"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://microservices:dev_2022@localhost:3306/micro_user_dev'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    # ENV = "production"
    # DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cloudacademy:pfm_2020@user-db:3306/user'
    # SQLALCHEMY_ECHO = False
	pass