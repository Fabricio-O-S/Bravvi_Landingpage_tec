import os
from dotenv import load_dotenv

# Encontra a pasta raiz para carregar o .env caso seja executado de subpastas
base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(base_dir, '.env'))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key_bravvi')
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI or SQLALCHEMY_DATABASE_URI.startswith('sqlite:///data/'):
        # Converte para caminho absoluto para evitar erros de diretório de trabalho relativo (especialmente em testes)
        data_dir = os.path.join(base_dir, 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        # Em Windows, o caminho absoluto do SQLite precisa de 3 barras seguidas pelo caminho absoluto (com barras normais)
        abs_path = os.path.abspath(os.path.join(data_dir, 'leads.db')).replace('\\', '/')
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{abs_path}"
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
