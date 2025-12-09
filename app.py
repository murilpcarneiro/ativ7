from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Configuração do banco de dados SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'natal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de dados para a lista de presentes
class Presente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    destinatario = db.Column(db.String(200), nullable=False)
    prioridade = db.Column(db.String(50), default='média')
    concluido = db.Column(db.Boolean, default=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'destinatario': self.destinatario,
            'prioridade': self.prioridade,
            'concluido': self.concluido,
            'data_criacao': self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')
        }

# Criar tabelas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/presentes', methods=['GET'])
def get_presentes():
    presentes = Presente.query.order_by(Presente.data_criacao.desc()).all()
    return jsonify([p.to_dict() for p in presentes])

@app.route('/api/presentes', methods=['POST'])
def adicionar_presente():
    dados = request.get_json()

    novo_presente = Presente(
        nome=dados.get('nome'),
        destinatario=dados.get('destinatario'),
        prioridade=dados.get('prioridade', 'média')
    )

    try:
        db.session.add(novo_presente)
        db.session.commit()
        return jsonify(novo_presente.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

@app.route('/api/presentes/<int:id>', methods=['PUT'])
def atualizar_presente(id):
    presente = Presente.query.get_or_404(id)
    dados = request.get_json()

    try:
        presente.nome = dados.get('nome', presente.nome)
        presente.destinatario = dados.get('destinatario', presente.destinatario)
        presente.prioridade = dados.get('prioridade', presente.prioridade)
        presente.concluido = dados.get('concluido', presente.concluido)

        db.session.commit()
        return jsonify(presente.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

@app.route('/api/presentes/<int:id>', methods=['DELETE'])
def deletar_presente(id):
    presente = Presente.query.get_or_404(id)

    try:
        db.session.delete(presente)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400

@app.route('/api/estatisticas', methods=['GET'])
def get_estatisticas():
    total = Presente.query.count()
    concluidos = Presente.query.filter_by(concluido=True).count()

    return jsonify({
        'total': total,
        'concluidos': concluidos,
        'pendentes': total - concluidos
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
