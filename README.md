# Bravvi Leadpages - Landing Page da Bravvi Tec

Este projeto consiste em uma página de captura (Leadpage) de alta conversão para a **Bravvi Tec**, desenvolvida com **Flask** no back-end e **Tailwind CSS** no front-end, seguindo uma arquitetura limpa, modular e profissional.

O design foi baseado no modelo de excelência corporativa (Opção 2) utilizando a paleta de Azul Marinho e Vermelho Acobreado como cores principais, com layouts modernos (Bento Grid) e animações suaves na rolagem.

---

## 🏗️ Arquitetura do Projeto

O projeto segue a seguinte estrutura profissional de pastas:

* `src/`: Código-fonte da aplicação Python (arquitetura MVC e rotas organizadas).
  * `app.py`: Ponto de entrada que inicializa o Flask, configura logs rotativos e gerencia o contexto do banco.
  * `models.py`: Modelo SQLAlchemy representando a tabela `Lead`.
  * `routes/`: Controlador modular utilizando Flask Blueprints.
* `templates/`: Arquivos HTML5 utilizando Jinja2 para reaproveitamento de blocos.
  * `base.html`: Estrutura base carregando fontes, ícones, Tailwind CSS e SweetAlert2.
  * `index.html`: Página principal com as seções institucionais e formulário de contato.
* `static/`: Recursos estáticos do front-end.
  * `css/style.css`: Estilizações finas de animação e Grid Bento.
  * `js/main.js`: Máscara dinâmica de telefone, validação client-side e envio AJAX.
  * `images/`: Logotipos horizontais e ícones em alta qualidade.
* `config/`: Configurações de ambiente seguros e banco de dados.
  * `db_config.py`: Carregador do python-dotenv e parametrização do banco de dados (absoluto para SQLite).
  * `.env.example`: Modelo de variáveis de ambiente.
* `data/`: Local de persistência do banco de dados local SQLite (`leads.db`).
* `logs/`: Histórico de erros e operações da aplicação (`app.log`).
* `tests/`: Scripts de testes automatizados (`test_app.py`).

---

## ⚙️ Instalação e Execução Local

### 1. Clonar o repositório
```bash
git clone https://github.com/Fabricio-O-S/Bravvi_Leadpages.git
cd Bravvi_Leadpages
```

### 2. Configurar o Ambiente Virtual (.venv)
```bash
python -m venv .venv
# Ativar no Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Ou no CMD:
.venv\Scripts\activate.bat
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto baseado no `.env.example`:
```env
FLASK_APP=src/app.py
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=sqlite:///data/leads.db
```

### 5. Executar a Aplicação
```bash
python -m src.app
```
Acesse o site em: `http://127.0.0.1:5000`

### 6. Executar Testes Automatizados
```bash
python -m unittest tests/test_app.py
```

---

## 🧠 O que aprendi

Durante o desenvolvimento deste projeto, aprofundei meus conhecimentos práticos em:

* **Arquitetura Limpa com Flask Blueprints**: Aprendi a modularizar as rotas do Flask em pacotes separados, mantendo o arquivo `app.py` magro e focado em inicializações e configurações da aplicação.
* **Persistência de Dados e Validações Seguras**: Implementei o ORM SQLAlchemy para gerenciar a persistência de leads em banco SQLite com tratamento de erros preventivo (`try/except` com gravação de logs detalhados e rollback de sessões).
* **Tratamento de Caminhos Absolutos para SQLite**: Configurei a string de conexão do SQLite de modo a converter caminhos relativos em caminhos de arquivo absolutos dinamicamente, evitando erros operacionais ao executar testes ou servidores a partir de diretórios de trabalho distintos.
* **Componentização Front-End Moderno (Bento Grid)**: Apliquei padrões modernos de layout (Bento Grid) utilizando Tailwind CSS, criando cards dinâmicos que se adaptam responsivamente a dispositivos móveis e desktop.
* **Experiência do Usuário (UX) Avançada com SweetAlert2 e AJAX**: Desenvolvi interações de formulário 100% assíncronas via `fetch` API no JavaScript, fornecendo feedbacks visuais com animações de carregamento (spinners) e modais interativos premium para o usuário final, com validação redundante no cliente e no servidor.
* **Logs Rotativos (Segurança e Resiliência)**: Configurei o `RotatingFileHandler` do Python para gravar execuções do servidor em arquivos de log limitados a 1MB, garantindo que o disco do servidor não sature com o tempo.
