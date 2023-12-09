class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.tarefas_atribuidas = []

    # Adiciona tarefa vinculada ao usuário
    def adicionar_tarefa(self, tarefa):
        self.tarefas_atribuidas.append(tarefa)
