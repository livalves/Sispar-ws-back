from src.model import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DECIMAL, Date
from sqlalchemy import text

class Reembolso(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    colaborador = Column(String(200), nullable=False)
    empresa = Column(String(50), nullable=False)
    num_prestacao = Column(Integer, nullable=False)
    descricao = Column(String(255))
    data = Column(Date, nullable=False, server_default=text('(CURRENT_DATE)'))
    tipo_reembolso = Column(String(30), nullable=False)
    centro_custo = Column(String(100), nullable=False)
    ordem_interna = Column(Integer)
    divisao = Column(Integer)
    pep = Column(Integer)
    moeda = Column(String(10), nullable=False)
    distancia_km = Column(DECIMAL(10,2))
    valor_km = Column(DECIMAL(10,2))
    valor_faturado = Column(DECIMAL(10,2), nullable=False)
    despesa = Column(DECIMAL(10,2)) # Valor taxa
    id_colaborador = Column(Integer, ForeignKey(column='colaborador.id'), nullable=False)
    status = Column(String(30), nullable=False) 

    def __init__(self, colaborador, empresa, num_prestacao, descricao, data, tipo_reembolso, centro_custo, ordem_interna, divisao, pep, moeda, distancia_km, valor_km, valor_faturado, despesa, id_colaborador, status='Em analise'):
        
        self.colaborador = colaborador
        self.empresa = empresa
        self.num_prestacao = num_prestacao
        self.descricao = descricao
        self.data = data
        self.tipo_reembolso = tipo_reembolso
        self.centro_custo = centro_custo
        self.ordem_interna = ordem_interna
        self.divisao = divisao
        self.pep = pep
        self.moeda = moeda
        self.distancia_km = distancia_km
        self.valor_km = valor_km
        self.valor_faturado = valor_faturado
        self.despesa = despesa
        self.id_colaborador = id_colaborador
        self.status = status
    
    def all_data(self) -> dict: 
        return {
            'id': self.id,
            'colaborador': self.colaborador,
            'empresa': self.empresa,
            'num_prestacao': self.num_prestacao,
            'descricao': self.descricao,
            'data': self.data.isoformat(),
            'tipo_reembolso': self.tipo_reembolso,
            'centro_custo': self.centro_custo,
            'ordem_interna': self.ordem_interna,
            'divisao': self.divisao,
            'pep': self.pep,
            'moeda': self.moeda,
            'distancia_km': self.distancia_km,
            'valor_km': self.valor_km,
            'valor_faturado': self.valor_faturado,
            'despesa': self.despesa,
            'id_colaborador': self.id_colaborador,
            'status': self.status
        }