#2 rotas 
#visualização de todos os reembolsos
#id_colaborador = padrão de id do colaborador  GET
# solicitação do reembolso  POST
# db.session.bulk_save_objects(Lista dos json)
# id = 298  - ID_COLABORADOR 

from flask import Blueprint, request, jsonify
from src.model import db
from src.model.reembolso_model import Reembolso
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

#from src.security.security import hash_senha, checar_senha


bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolsos')

@bp_reembolso.route('/envio-para-analise', methods=['POST'])
@jwt_required()
def cadastrar_novo_reembolso():
    data = request.get_json()
    id_colaborador = get_jwt_identity()
    
    novo_reembolso = Reembolso(
        colaborador=data['colaborador'],
        empresa=data['empresa'],
        num_prestacao=data['num_prestacao'],
        descricao=data['descricao'],
        data=data['data'],
        tipo_reembolso=data['tipo_reembolso'],
        centro_custo=data['centro_custo'],
        ordem_interna=data['ordem_interna'],
        divisao=data['divisao'],
        pep=data['pep'],
        moeda=data['moeda'],
        distancia_km=data['distancia_km'],
        valor_km=data['valor_km'],
        valor_faturado=data['valor_faturado'],
        despesa=data['despesa'],
        id_colaborador=id_colaborador,
        status='Em analise'
    )
    db.session.add(novo_reembolso)
    db.session.commit()
    
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'} ), 201

@bp_reembolso.route('/solicitacao/<int:id>', methods=['GET'])
@jwt_required()
def visualizar_reembolso_nprestacao(id):
    id_colaborador = get_jwt_identity()
    reembolso = Reembolso.query.filter_by(id=id, id_colaborador=id_colaborador).first()
    
    if not reembolso:
        return jsonify({'mensagem': 'Reembolso não encontrado'}), 404
    
    return jsonify(reembolso.all_dict()), 200
