from flask import Flask
from config import config

from flask_login import LoginManager
# ... outras importações ...

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Inicialização de extensões, como SQLAlchemy, se estiver usando
    # db.init_app(app)

    login_manager.init_app(app)

    # Registro de blueprints
    from .modulos.clientes import clientes as clientes_blueprint
    app.register_blueprint(clientes_blueprint, url_prefix='/clientes')

    # Repita o registro para outros blueprints

    return app




