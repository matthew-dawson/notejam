from notejam import app
from notejam.config import DevelopmentConfig
from notejam.config import ProductionConfig
from notejam.config import TestingConfig
import os

if __name__ == '__main__':
    environment = os.getenv('ENVIRONMENT', 'TESTING')
    sql_uri = os.getenv('SQL_URI')


    if environment == 'development':
        app.config.from_object(DevelopmentConfig)
        app.config.SQLALCHEMY_DATABASE_URI = sql_uri
    elif environment == 'production':
        app.config.from_object(ProductionConfig)
        app.config.SQLALCHEMY_DATABASE_URI = sql_uri

    app.run("0.0.0.0")