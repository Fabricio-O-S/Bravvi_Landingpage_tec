import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config.db_config import Config
from src.models import db
from src.routes.main import main_bp

def create_app(config_class=Config):
    """
    Factory function para criação do app Flask.
    Configura segurança, banco de dados, logs e registra blueprints.
    """
    app = Flask(__name__, 
                template_folder='../templates', 
                static_folder='../static')
    
    app.config.from_object(config_class)

    # Inicialização do Banco de Dados
    db.init_app(app)

    # Registro de Blueprints
    app.register_blueprint(main_bp)

    # Configuração de Logs
    setup_logging(app)

    # Criação das tabelas no banco de dados SQLite local
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Tabelas do banco de dados inicializadas/verificadas com sucesso.")
        except Exception as e:
            app.logger.error(f"Erro ao inicializar tabelas do banco de dados: {e}")

    return app

def setup_logging(app):
    """Configura o sistema de logs gravando erros e acessos em logs/app.log."""
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'app.log')
    
    # Gerenciador de log rotativo (limite de 1MB por arquivo, mantém até 3 arquivos)
    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=3, encoding='utf-8')
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s em %(module)s [%(pathname)s:%(lineno)d]: %(message)s'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Logger do Flask
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    # Logger personalizado para a aplicação
    app_logger = logging.getLogger('bravvi_app')
    app_logger.addHandler(file_handler)
    app_logger.setLevel(logging.INFO)

    app.logger.info("Sistema de logs da Bravvi Tec inicializado com sucesso.")

app = create_app()

if __name__ == '__main__':
    # Roda o servidor localmente
    # Porta padrão do Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
