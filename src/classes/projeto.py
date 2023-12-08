from Tarefa import Tarefa

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        # Adiciona uma tarefa ao projeto
        self.tarefas.append(tarefa)
        Tarefa.salvar_tarefas_em_json(self.tarefas)

    def ver_status_geral(self):
        # Implemente conforme necessário
        pass

    def criar_tarefa(self, titulo, descricao, status, data_criacao, data_conclusao=None):
        # Cria uma nova tarefa e a adiciona ao projeto
        nova_tarefa = Tarefa(titulo, descricao, status, data_criacao, data_conclusao)
        self.tarefas.append(nova_tarefa)
        Tarefa.salvar_tarefas_em_json(self.tarefas)
        return nova_tarefa

    def alterar_status_tarefa(self, tarefa, novo_status):
        # Altera o status de uma tarefa
        tarefa.status = novo_status
        Tarefa.salvar_tarefas_em_json(self.tarefas)

    def adicionar_tarefa(self, tarefa):
        # Adiciona uma tarefa ao projeto
        self.tarefas.append(tarefa)
        Tarefa.salvar_tarefas_em_json(self.tarefas)

    def ver_status_geral(self):
        # Implemente conforme necessário
        pass
