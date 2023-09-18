from decouple import config

from dotenv import dotenv_values

vars = dotenv_values(".env")

class Config:
    SECRET_KEY = "easypass"

db_password = vars["ROOT_PASSWORD"]

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{db_password}@localhost/project_web_easy"
    #SQLALCHEMY_TRACK_MODODIFICATIONS = False #en caso de tener este error

    MAIL_SERVER = vars["PROJECT_MAIL_SERVER"]
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = vars["PROJECT_MAIL_USERNAME"]
    MAIL_PASSWORD = vars["PROJECT_MAIL_PASSWORD"]
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}