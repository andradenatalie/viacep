from flask import Flask
from flasgger import Swagger
from app.adapters.database import db
from app.controllers.endereco_controller import endereco_bp
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Inicializa o banco de dados
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    # Configuração do Swagger
    template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Endereços",
            "description": "API para gerenciar endereços via CEP",
            "version": "1.0.0"
        },
        "host": "localhost:8080",  # Alterar se for rodar em outro host
        "basePath": "/",
        "schemes": ["http"]
    }

    Swagger(app, template=template)

    app.register_blueprint(endereco_bp)

    return app