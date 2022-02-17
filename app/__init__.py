from flask import Flask
from flask_bootstrap import Bootstrap
from .main import main,views
from .request import configure_request
from config import config_options
from .news import News


 # Initializing Flask Extensions
bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.register_blueprint(main)
    app.config.from_object(config_options[config_name])
    #....
    # app.register_blueprint(main)
    configure_request(app)
    bootstrap.init_app(app)
    return app

   

# Registering the blueprint
   


    # setting config
   







