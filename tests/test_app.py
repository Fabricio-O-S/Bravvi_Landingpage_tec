import json
import unittest
from src.app import create_app
from src.models import db, Lead
from config.db_config import Config

class TestConfig(Config):
    """Configuração de testes específica (banco em memória)."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'test_secret_key'

class BravviLeadpagesTestCase(unittest.TestCase):
    """Conjunto de testes para a aplicação Bravvi Leadpages."""

    def setUp(self):
        """Inicializa o app com banco em memória antes de cada teste."""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        """Limpa as tabelas e remove o contexto após cada teste."""
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_index_page_loads(self):
        """Verifica se a landing page carrega com sucesso."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bravvi Tec', response.data)
        self.assertIn(b'Liderando a Inovacao', response.data.replace(b'\xc3\xa7\xc3\xa3', b'ca'))

    def test_submit_valid_lead(self):
        """Testa o cadastro com dados válidos (deve retornar 201)."""
        payload = {
            'name': 'Fabricio Oliveira',
            'email': 'fabricio@bravvitec.com',
            'whatsapp': '(11) 99999-9999',
            'industry': 'Software',
            'message': 'Gostaria de agendar uma demonstração do sistema.'
        }
        response = self.client.post(
            '/submit-lead',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        
        # Verifica se foi gravado no banco de dados
        lead = Lead.query.filter_by(email='fabricio@bravvitec.com').first()
        self.assertIsNotNone(lead)
        self.assertEqual(lead.name, 'Fabricio Oliveira')
        self.assertEqual(lead.industry, 'Software')

    def test_submit_invalid_email(self):
        """Testa validação de e-mail incorreto (deve retornar 400)."""
        payload = {
            'name': 'Fabricio Oliveira',
            'email': 'email-invalido',
            'whatsapp': '(11) 99999-9999',
            'industry': 'Software',
            'message': 'Mensagem qualquer.'
        }
        response = self.client.post(
            '/submit-lead',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertIn('O e-mail fornecido é inválido.', data['errors'])

    def test_submit_missing_field(self):
        """Testa validação de campos vazios/ausentes (deve retornar 400)."""
        payload = {
            'name': '',
            'email': 'fabricio@bravvitec.com',
            'whatsapp': '',
            'industry': '',
            'message': ''
        }
        response = self.client.post(
            '/submit-lead',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertTrue(len(data['errors']) > 0)

if __name__ == '__main__':
    unittest.main()
