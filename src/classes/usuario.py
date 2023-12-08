from classes.Tarefa import Tarefa

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.tarefas_atribuidas = []

    def criar_tarefa(self, titulo, descricao, status, data_criacao, data_conclusao=None):
        nova_tarefa = Tarefa(titulo, descricao, status, data_criacao, data_conclusao)
        self.tarefas_atribuidas.append(nova_tarefa)
        Tarefa.salvar_tarefas_em_json(self.tarefas_atribuidas)
        return nova_tarefa

    def alterar_status_tarefa(self, tarefa, novo_status):
        tarefa.status = novo_status
        Tarefa.salvar_tarefas_em_json(self.tarefas_atribuidas)
