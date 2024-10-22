from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialização do Flask
app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tarcio:BamSMksHbvp0QNmC3MI2JG947fyhCMA1@dpg-crs0kkjtq21c73dagm4g-a.oregon-postgres.render.com:5432/db_senior_care'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilita notificações de modificações de objetos

# Instância do SQLAlchemy
db = SQLAlchemy(app)
