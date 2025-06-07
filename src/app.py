from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger
from flask_jwt_extended import JWTManager

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

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Sispar",
        "description": "Documentação da API de colaboradores e reembolsos",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Adicione 'Bearer <seu_token_jwt>'"
        }
    },
    "security": [{"Bearer": []}]
}


jwt = JWTManager()

def create_app():
    app = Flask(__name__) 
    
    app.config.from_object(Config)
    
    CORS(app, origins="*")  # Provisorio
       
    db.init_app(app) 
    jwt.init_app(app)
    
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_reembolso)
    
    with app.app_context(): 
        db.create_all()
    
    #Swagger(app, config=swagger_config)
    Swagger(app, config=swagger_config, template=swagger_template)
    
    return app    