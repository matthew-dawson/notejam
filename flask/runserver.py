from notejam import app
from notejam.config import DevelopmentConfig

#TODO: Determine environment based upon environment variable
app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    app.run("0.0.0.0")
