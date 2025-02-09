# Api-em-Python

Esta é uma API simples em Python utilizando Flask e SQLAlchemy para gerenciar contatos.

## Estrutura do Projeto

## Configuração

### Pré-requisitos

- Python 3.10+
- PostgreSQL

### Instalação

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd Api-em-Python
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados PostgreSQL no arquivo [config.py](http://_vscodecontentref_/4):
    ```py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>'
    ```

## Uso

1. Inicie a aplicação:
    ```sh
    python app.py
    ```

2. Acesse a API em `http://127.0.0.1:5000`.

## Endpoints

### GET /contacts

Retorna todos os contatos.

### GET /contacts/<int:contact_id>

Retorna um contato específico pelo ID.

### POST /contacts

Cria um novo contato. Exemplo de payload:
```json
{
    "nome": "Jane Doe",
    "endereco": "456 Elm St",
    "idade": 25,
    "email": "jane.doe@example.com",
    "telefone": "987-654-3210"
}
```
