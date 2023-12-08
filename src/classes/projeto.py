from classes.Tarefa import Tarefa

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        Tarefa.salvar_tarefas_em_json(self.tarefas)

    def ver_status_geral(self):
        if self.tarefas:
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i+1}. {tarefa.titulo} - {tarefa.status}")
        else:
            print("O projeto não tem tarefas.")

    def criar_tarefa(self, titulo, descricao, status, data_criacao, data_conclusao=None):
        nova_tarefa = Tarefa(titulo, descricao, status, data_criacao, data_conclusao)
        self.adicionar_tarefa(nova_tarefa)
        return nova_tarefa

    def alterar_status_tarefa(self, tarefa, novo_status):
        tarefa.status = novo_status
        Tarefa.salvar_tarefas_em_json(self.tarefas)
