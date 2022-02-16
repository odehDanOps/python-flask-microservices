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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost:3306/micro_product_dev'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://danops:danops_2022@host.docker.internal:3306/product'
    SQLALCHEMY_ECHO = False