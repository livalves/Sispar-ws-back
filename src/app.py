from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec", # <-- Da um nome de referencia para a documentacao
            "route": "/apispec.json/", # <- Rota do arquivo JSON para a construção da documentação
            "rule_filter": lambda rule: True, # <-- Todas as rotas/endpoints serão documentados
            "model_filter": lambda tag: True, # <-- Especificar quuais modelos da entidade serão documentados
        }
    ],
    "static_url_path": "/flasgger_static", # <-- Rota para acessar a documentação
    "swagger_ui": True, # <-- Ativa a interface Swagger UI
    "specs_route": "/apidocs/", # <-- Rota para acessar a documentação
}

def create_app():
    app = Flask(__name__) 
    CORS(app, origins="*")  # Provisorio
    app.register_blueprint(bp_colaborador)
    
    app.config.from_object(Config)
    db.init_app(app) 
    
    with app.app_context(): 
        db.create_all()
    
    Swagger(app, config=swagger_config)
    
    return app    