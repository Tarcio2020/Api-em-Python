# API em Python

Esta é uma API simples em Python utilizando **Flask** e **SQLAlchemy** para gerenciar contatos.

## Estrutura do Projeto

O projeto é estruturado da seguinte maneira:
- **app.py**: arquivo principal da aplicação.
- **service.py**: camada de serviço que manipula a lógica de negócios.
- **models.py**: define os modelos do banco de dados (por exemplo, o modelo de Contato).
- **config.py**: configurações da aplicação, como a URI do banco de dados.
- **requirements.txt**: lista das dependências do projeto.

## Configuração

### Pré-requisitos

- Python 3.10+
- PostgreSQL

### Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/Tarcio2020/Api-em-Python.git
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

4. Configure o banco de dados PostgreSQL no arquivo [config.py](config.py):
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>'
    ```

## Uso

1. Inicie a aplicação:
    ```sh
    python app.py
    ```

2. Acesse a API em `http://127.0.0.1:5000`.

## Endpoints

### **GET /contacts**

**Descrição**: Retorna todos os contatos cadastrados.

**Exemplo de resposta**:
```json
[
    {
        "id": 1,
        "nome": "John Doe",
        "endereco": "123 Main St",
        "idade": 30,
        "email": "john.doe@example.com",
        "telefone": "123-456-7890"
    },
    {
        "id": 2,
        "nome": "Jane Doe",
        "endereco": "456 Elm St",
        "idade": 25,
        "email": "jane.doe@example.com",
        "telefone": "987-654-3210"
    }
]
```

### **GET /contacts/<int:contact_id>**

**Descrição**: Retorna um contato específico pelo **ID**.

**Parâmetros**:
- `contact_id` (int): O ID do contato a ser retornado.

**Exemplo de resposta**:
```json
{
    "id": 1,
    "nome": "John Doe",
    "endereco": "123 Main St",
    "idade": 30,
    "email": "john.doe@example.com",
    "telefone": "123-456-7890"
}
```

**Resposta de erro (se o contato não for encontrado)**:
```json
{
    "error": "Contact not found"
}
```

### **POST /contacts**

**Descrição**: Cria um novo contato.

**Exemplo de payload**:
```json
{
    "nome": "Jane Doe",
    "endereco": "456 Elm St",
    "idade": 25,
    "email": "jane.doe@example.com",
    "telefone": "987-654-3210"
}
```

**Exemplo de resposta**:
```json
{
    "id": 3,
    "nome": "Jane Doe",
    "endereco": "456 Elm St",
    "idade": 25,
    "email": "jane.doe@example.com",
    "telefone": "987-654-3210"
}
```

**Código de status**: `201 Created`

### **PUT /contacts/<int:contact_id>**

**Descrição**: Atualiza as informações de um contato existente.

**Parâmetros**:
- `contact_id` (int): O ID do contato a ser atualizado.

**Exemplo de payload**:
```json
{
    "nome": "Jane Smith",
    "endereco": "456 Elm St",
    "idade": 26,
    "email": "jane.smith@example.com",
    "telefone": "987-654-3210"
}
```

**Exemplo de resposta**:
```json
{
    "id": 3,
    "nome": "Jane Smith",
    "endereco": "456 Elm St",
    "idade": 26,
    "email": "jane.smith@example.com",
    "telefone": "987-654-3210"
}
```

**Resposta de erro (se o contato não for encontrado)**:
```json
{
    "error": "Contact not found"
}
```

### **DELETE /contacts/<int:contact_id>**

**Descrição**: Deleta um contato específico pelo **ID**.

**Parâmetros**:
- `contact_id` (int): O ID do contato a ser deletado.

**Exemplo de resposta**:
```json
{
    "message": "Contact deleted"
}
```

**Resposta de erro (se o contato não for encontrado)**:
```json
{
    "error": "Contact not found"
}
```

---

