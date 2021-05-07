from notejam import app
from notejam.config import DevelopmentConfig
from notejam.config import ProductionConfig
from notejam.config import TestingConfig
import os

if __name__ == '__main__':
    environment = os.getenv('ENVIRONMENT', 'TESTING')

    if environment == 'development':
        print("Development environment, loading development config")
        app.config.from_object(DevelopmentConfig)

    elif environment == 'production':
        print("Production environment, loading production config")
        app.config.from_object(ProductionConfig)


    app.run("0.0.0.0")