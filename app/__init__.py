from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timezone

# Instâncias do SQLAlchemy e Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/teclatdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar as extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Importa as rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
