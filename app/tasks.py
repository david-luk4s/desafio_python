from flask import jsonify
from .models import Tarefa
from . import db
from datetime import datetime


def add_task(data):
    task_name = data.get('taskName')
    task_description = data.get('taskDescription')
    
    if task_name and task_description:
        nova_tarefa = Tarefa(titulo=task_name, descricao=task_description)
        db.session.add(nova_tarefa)
        db.session.commit()
        
        data_criacao = nova_tarefa.data_criacao if nova_tarefa.data_criacao else datetime.now()
        data_formatada = data_criacao.strftime('%d/%m/%Y %H:%M:%S')

        response = {
            'id': nova_tarefa.id,
            'titulo': nova_tarefa.titulo,
            'descricao': nova_tarefa.descricao,
            'status_conclusao': nova_tarefa.status_conclusao,
            'data_criacao': data_formatada,
            'data_status_conclusao': nova_tarefa.data_status_conclusao.strftime('%d/%m/%Y %H:%M:%S') if nova_tarefa.data_status_conclusao else None
        }
        return jsonify(response), 201
    else:
        return jsonify({'error': 'Nome e descrição da tarefa são obrigatórios.'}), 400

def update_task(task_id, data):
    task = Tarefa.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Tarefa não encontrada.'}), 404
    
    task.titulo = data.get('taskTitle')
    task.descricao = data.get('taskDescription')
    
    if data.get('taskStatus'):
        task.concluir()
    else:
        task.status_conclusao = False
        task.data_status_conclusao = None
    
    db.session.commit()
    
    response = {
        'id': task.id,
        'titulo': task.titulo,
        'descricao': task.descricao,
        'status_conclusao': task.status_conclusao,
        'data_status_conclusao': task.data_status_conclusao.strftime('%d/%m/%Y %H:%M:%S') if task.data_status_conclusao else None
    }
    return jsonify(response)

def delete_task(task_id):
    tarefa = Tarefa.query.get(task_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa excluída com sucesso!'}), 200
    return jsonify({'message': 'Tarefa não encontrada!'}), 404
