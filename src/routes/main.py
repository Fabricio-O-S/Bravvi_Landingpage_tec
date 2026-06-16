import re
import logging
from flask import Blueprint, render_template, request, jsonify
from src.models import db, Lead

# Blueprint para rotas principais
main_bp = Blueprint('main', __name__)

# Configuração de logger específico para as rotas
logger = logging.getLogger('bravvi_app')

def is_valid_email(email):
    """Valida formato de e-mail básico."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_whatsapp(phone):
    """Valida telefone/WhatsApp (deve conter apenas números e tamanho mínimo)."""
    # Remove caracteres especiais para validação
    cleaned = re.sub(r'\D', '', phone)
    return len(cleaned) >= 10

@main_bp.route('/')
def index():
    """Renderiza a Landing Page da Bravvi Tec."""
    return render_template('index.html')

@main_bp.route('/submit-lead', methods=['POST'])
def submit_lead():
    """
    Processa o envio assíncrono do formulário de captura de leads.
    Valida os dados e insere no banco de dados SQLite local.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'Dados não fornecidos.'}), 400

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        whatsapp = data.get('whatsapp', '').strip()
        industry = data.get('industry', '').strip()
        message = data.get('message', '').strip()

        # Validações de campos obrigatórios
        errors = []
        if not name:
            errors.append('O campo Nome é obrigatório.')
        if not email:
            errors.append('O campo E-mail é obrigatório.')
        elif not is_valid_email(email):
            errors.append('O e-mail fornecido é inválido.')
        if not whatsapp:
            errors.append('O campo WhatsApp é obrigatório.')
        elif not is_valid_whatsapp(whatsapp):
            errors.append('O WhatsApp fornecido é inválido (mínimo de 10 dígitos).')
        if not industry:
            errors.append('Por favor, selecione uma Indústria.')
        if not message:
            errors.append('O campo Mensagem é obrigatório.')

        if errors:
            logger.warning(f"Tentativa de submissão de lead inválido: {errors}")
            return jsonify({'status': 'error', 'errors': errors}), 400

        # Criação e persistência do lead
        new_lead = Lead(
            name=name,
            email=email,
            whatsapp=whatsapp,
            industry=industry,
            message=message
        )
        db.session.add(new_lead)
        db.session.commit()

        logger.info(f"Novo lead capturado com sucesso: {email} | Indústria: {industry}")
        return jsonify({
            'status': 'success',
            'message': 'Sua solicitação foi enviada com sucesso! Nossos consultores entrarão em contato em breve.'
        }), 201

    except Exception as e:
        db.session.rollback()
        logger.exception("Erro interno ao salvar lead no banco de dados:")
        return jsonify({
            'status': 'error',
            'message': 'Ocorreu um erro no servidor ao processar seu cadastro. Tente novamente mais tarde.'
        }), 500
