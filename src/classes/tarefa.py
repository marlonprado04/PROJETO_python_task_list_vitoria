import datetime


class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Pendente"
        self.data_criacao = datetime.date.today()
        self.data_conclusao = None
        self.usuario = None
        self.projeto = None

    def concluir_tarefa(self):
        self.status = "Concluída"
        self.data_conclusao = datetime.date.today()

    def atribuir_usuario(self, usuario):
        self.usuario = usuario

    def atribuir_projeto(self, projeto):
        self.projeto = projeto
    
    def __str__(self):
        return f"Tarefa: {self.titulo}, Status: {self.status}"
