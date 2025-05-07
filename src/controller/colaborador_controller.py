from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

#dados = [
#        {'id': 1,'nome': 'Karynne Moreira', 'cargo': 'CEO', 'cracha': '010101'},
#        {'id': 2,'nome': 'Samuel Silverio', 'cargo': 'CTO', 'cracha': '74512'},
#        {'id': 3,'nome': 'Thales Reis', 'cargo': 'Desenvolvedor Back-end Java', 'cracha': '14523'},
#        {'id': 4,'nome': 'Eduardo Gomes', 'cargo': 'DevOps', 'cracha': '78412'},
#        {'id': 5,'nome': 'Gabriel Silvano', 'cargo': 'Desenvolvedor Front-end React', 'cracha': '96523'},
#        {'id': 6,'nome': 'Suelen Braga', 'cargo': 'Infra', 'cracha': '251473'}
#    ]

#@bp_colaborador.route('/pegar-dados')
#def pegar_dados():
#    return dados

@bp_colaborador.route('/todos-colaboradores', methods=['GET'])
def pegar_dados_todos_colaboradores():
    colaboradores = db.session.execute(
        db.select(Colaborador)
    ).scalars().all()
    
    colaboradores = [ colaborador.all_data() for colaborador in colaboradores ]
    
    return jsonify(colaboradores), 200


# TAREFA -> VALIDAÇÃO DO CAMPO CRACHA. NÃO PODEMOS TER DUPLICATAS


@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from('../docs/colaborador/cadastrar_colaborador.yml')
def cadastrar_novo_colaborador(): 
    dados_requisicao = request.get_json() 
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'], 
        email=dados_requisicao['email'],
        senha=hash_senha(dados_requisicao['senha']),
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
    db.session.add(novo_colaborador)
    db.session.commit() 
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'} ), 201


# TAREFA -> VALIDAÇÃO DO USUARIO. VERIFICAÇÃO DE USUARIO NO BANCO DE DADOS (MOCKADO)


@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_do_colaborador(id_colaborador):
    
    dados_requisicao = request.get_json()
    
    #for colaborador in dados:
    for colaborador in dados_requisicao:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break 
    
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']
    if 'cracha' in dados_requisicao:
        colaborador_encontrado['cracha'] = dados_requisicao['cracha']

    return jsonify({'mensagem': 'Dados do colaborador atualizados com sucesso'}), 200

@bp_colaborador.route('/login', methods=['POST'])
def login():
    
    dados_requisicao = request.get_json()
    
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
    
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os dados precisam ser preenchidos!'}), 400
    
    # SELECT * FROM [TABELA]
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.email == email)
    ).scalar() 
    
    #print('*'*100)
    #print(f'dado: {colaborador} é do tipo {type(colaborador)}')
    #print('*'*100)
    
    if not colaborador:
        return jsonify({'mensagem': 'Usuario não encontrado'}), 404
    
    colaborador = colaborador.to_dict()
    
    #print('*'*100)
    #print(f'dado: {colaborador} é do tipo {type(colaborador)}')
    #print('*'*100)
    
    #if email == colaborador.get('email') and checar_senha(senha, colaborador.get('senha')):
    #    return jsonify({'mensagem': 'Login realizado com sucesso'}), 200
    #else:
    #    return jsonify({'mensagem': 'Credenciais invalidas'}), 400
    
    if colaborador.get('email') == email and checar_senha(senha, colaborador.get('senha')):
        return jsonify({'mensagem': 'Login realizado com sucesso'}), 200