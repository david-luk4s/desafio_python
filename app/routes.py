from flask import Blueprint, render_template, request, jsonify
from .models import Tarefa
from . import db
from .tasks import add_task, update_task, delete_task

bp = Blueprint('main', __name__)

# Rota principal
@bp.route('/')
def index():
    tarefas = Tarefa.query.order_by(Tarefa.data_criacao).all()
    return render_template('index.html', tarefas=tarefas, message='')

# Rota API para Criar Tarefa
@bp.route('/api/add_task', methods=['POST'])
def add_task_api():
    data = request.json
    return add_task(data)

# Rota API para Atualizar Tarefa
@bp.route('/api/update_task/<int:task_id>', methods=['POST'])
def update_task_api(task_id):
    data = request.json
    return update_task(task_id, data)

# Rota API para Deletar Tarefa
@bp.route('/api/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task_api(task_id):
    return delete_task(task_id)
