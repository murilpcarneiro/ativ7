# Usar imagem base Python 3.11
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expor a porta 5000
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]
