from datetime import datetime

class Tarefa:
    # Define atributos da tarefa
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Pendente"
        self.data_criacao = datetime.now()
        self.data_conclusao = None

    # Atualiza o status da tarefa
    def atualizar_status(self):
        self.status = "Finalizado"
        self.data_conclusao = datetime.now()

    # Atualiza a descrição da tarefa
    def atualizar_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    # Atualiza o título da tarefa
    def atualizar_titulo(self, novo_titulo):
        self.atualizar_titulo = novo_titulo

