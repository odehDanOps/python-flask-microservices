# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = 'LJNa5zTQ-5FZhTu8rxq1DSxClHp_Yg'
    WTF_CSRF_SECRET_KEY = 'Npk-XmP94F7tayngH1WrfWyXgg8pasDqyZvidIX7'


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False