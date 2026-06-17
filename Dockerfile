# Imagem base oficial do Python baseada na versão do runtime.txt
FROM python:3.11-slim

# Evita que o Python escreva arquivos .pyc no disco e mantém o buffer de log livre
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala ferramentas básicas de compilação necessárias para algumas libs python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas o requirements.txt para aproveitar o cache de camadas do Docker
COPY requirements.txt .

# Instala as dependências python do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código do projeto para o diretório de trabalho
COPY . .

# Expõe a porta configurada
EXPOSE 5000

# Executa o app usando o gunicorn como servidor de produção (idêntico ao Procfile)
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} src.app:app"]
