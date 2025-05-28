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
from datetime import datetime

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolsos')

@bp_reembolso.route('/envio-para-analise', methods=['POST'])
@jwt_required()
def cadastrar_novo_reembolso():
    
    #try:
    #    data_date = datetime.strptime(data['data'], '%Y-%m-%d').date()
    #except Exception as e:
    #    return jsonify({'mensagem': 'Formato de data inválido'}), 400
    
    data = request.get_json()
    
    if not isinstance(data, list):
        return jsonify({'mensagem': 'Esperado uma lista de reembolsos'}), 400

    required_fields = ['colaborador', 'empresa', 'num_prestacao', 'descricao', 'data',
                       'tipo_reembolso', 'centro_custo', 'ordem_interna', 'divisao',
                       'pep', 'moeda', 'distancia_km', 'valor_km', 'valor_faturado', 'despesa']
    
    id_colaborador = get_jwt_identity()

    
    lista_reembolsos = []
    
    for item in data:
        for field in required_fields:
            if field not in item:
                return jsonify({'mensagem': f'Campo obrigatório ausente: {field}'}), 400

        reembolso = Reembolso(
            colaborador=item['colaborador'],
            empresa=item['empresa'],
            num_prestacao=item['num_prestacao'],
            descricao=item['descricao'],
            data=item['data'],
            tipo_reembolso=item['tipo_reembolso'],
            centro_custo=item['centro_custo'],
            ordem_interna=item['ordem_interna'],
            divisao=item['divisao'],
            pep=item['pep'],
            moeda=item['moeda'],
            distancia_km=item['distancia_km'],
            valor_km=item['valor_km'],
            valor_faturado=item['valor_faturado'],
            despesa=item['despesa'],
            id_colaborador=id_colaborador,
            status='Em analise'
        )
        lista_reembolsos.append(reembolso)

    db.session.add(lista_reembolsos)
    db.session.commit()
    
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'} ), 201


@bp_reembolso.route('/solicitacao/todos', methods=['GET'])
@jwt_required()
def listar_reembolsos():
    id_colaborador = get_jwt_identity()
    reembolsos = Reembolso.query.filter_by(id_colaborador=id_colaborador).all()

    if not reembolsos:
        return jsonify({'mensagem': 'Nenhum reembolso encontrado'}), 404

    return jsonify([r.all_data() for r in reembolsos]), 200


@bp_reembolso.route('/solicitacao/<int:id>', methods=['GET'])
@jwt_required()
def visualizar_reembolso_nprestacao(id):
    id_colaborador = get_jwt_identity()
    reembolso = Reembolso.query.filter_by(id=id, id_colaborador=id_colaborador).first()
    
    if not reembolso:
        return jsonify({'mensagem': 'Reembolso não encontrado'}), 404
    
    return jsonify(reembolso.all_dict()), 200
