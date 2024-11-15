# Usar imagem base Python
FROM python:3.11-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Definir a variável de ambiente para o Flask (opcional, mas recomendável)
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expor a porta padrão do Flask
EXPOSE 5000

# Definir o comando de inicialização diretamente com Flask
CMD ["flask", "run", "--host=0.0.0.0"]
