class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.projetos = []

    def criar_projeto(self, nome, descricao):
        projeto = Projeto(nome, descricao)
        self.projetos.append(projeto)
        return projeto

    def atribuir_tarefa(self, projeto, tarefa):
        projeto.adicionar_tarefa(tarefa)
        tarefa.atribuir_usuario(self)

    def __str__(self):
        return f"Usuario: {self.nome}, Email: {self.email}"
