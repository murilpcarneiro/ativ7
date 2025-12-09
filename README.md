# 🎄 Aplicativo de Lista de Presentes de Natal 🎁

Aplicativo web para gerenciar lista de presentes de Natal, desenvolvido em Python com Flask.

## 📋 Funcionalidades

- ✅ Adicionar, editar e deletar presentes
- ✅ Classificar por prioridade (Alta, Média, Baixa)
- ✅ Marcar presentes como concluídos
- ✅ Interface web responsiva com tema natalino
- ✅ Banco de dados SQLite para persistência

## 🐳 Como Executar com Docker

```bash
# Carregar a imagem
docker load -i natal-app-v1.0.tar

# Executar
docker run -d -p 5000:5000 --name natal-app natal-app:v1.0

# Acessar em http://localhost:5000
```

## 🚀 Como Executar Localmente

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Executar
python app.py

# Acessar em http://localhost:5000
```

## 📁 Estrutura

```
├── app.py               # Aplicação Flask
├── requirements.txt     # Dependências
├── Dockerfile          # Configuração Docker
├── templates/
│   └── index.html      # Interface web
└── natal.db            # Banco de dados (criado automaticamente)
```

## 🛠️ Tecnologias

- Python 3.11
- Flask 2.3.3
- SQLite + SQLAlchemy
- HTML5, CSS3, JavaScript
