class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

    def status_geral(self):
        concluidas = sum(1 for tarefa in self.tarefas if tarefa.status == "Concluída")
        total = len(self.tarefas)
        return f"Projeto {self.nome}: {concluidas}/{total} tarefas concluídas"

    def __str__(self):
        return f"Projeto: {self.nome}, Descrição: {self.descricao}"
