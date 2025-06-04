# Sispar (Back-end)

**Sispar** é uma API RESTful desenvolvida em Python (Flask) como desafio final do curso de Desenvolvimento Full Stack da *Vai na Web*.  
O projeto propõe a remodelação do sistema utilizado pela **Wilson Sons**, com foco em modernizar a experiência do usuário, otimizar processos e aplicar boas práticas de desenvolvimento.

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-JWT-Extended (autenticação)
- SQLAlchemy (ORM)
- Flasgger (Swagger para documentação)
- MySQL (banco de dados relacional)

## 📦 Como clonar e rodar o projeto

### Pré-requisitos

- Python instalado (3.10+)
- MySQL instalado e rodando
- Git instalado

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/livalves/Sispar-ws-back.git
cd Sispar-ws-back
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
source venv/Scripts/activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` com as suas credenciais:

```env
URL_DATABASE_DEV="mysql://usuario:senha@localhost:3306/nomedobanco"
JWT_SECRET_KEY=sua_chave_secreta
```

5. Rode o servidor local:

```bash
python run.py
```

---

## 📌 Rotas principais da API

### 🔐 Autenticação

#### `POST /login`
- Realiza login com e-mail e senha.
- Retorna um token JWT.

---

### 👤 Colaboradores

#### `POST /colaboradores/cadastrar`
- Cadastra um novo colaborador.
- Exemplo de body:

```json
{
  "nome": "Ana Silva",
  "email": "ana@empresa.com",
  "senha": "senha123",
  "cargo": "Analista de Dados",
  "salario": 5000
}
```

#### `POST /colaboradores/todos-colaboradores`
- Retorna uma lista com todos os colaboradores cadastrados.

#### `POST /colaboradores/atualizar/<int:id_colaborador>`
- Atualiza os dados de um colaborador com base no _id_colaborador_.

---

### 💰 Reembolsos

#### `POST /reembolsos/envio-para-analise`
- Envia as solicitações de reembolso para análise (requer token JWT).

#### `GET /reembolsos/solicitacao/<num_prestacao>`
- Retorna uma solicitação específica de um colaborador pelo número de prestação (token necessário).

#### `GET /reembolsos/solicitacao/todos`
- Retorna todos os reembolsos do colaborador autenticado (token necessário).

---

## 🎯 Objetivos do Projeto

- Modernizar o sistema de reembolso utilizado pela Wilson Sons.
- Aprimorar usabilidade, segurança e performance.
- Aplicar conceitos sólidos de API RESTful.
- Praticar integração front-end e back-end.

