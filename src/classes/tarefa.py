class Tarefa:
    def __init__(self, titulo, descricao, status, data_criacao, data_conclusao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_criacao = data_criacao
        self.data_conclusao = data_conclusao

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'data_criacao': self.data_criacao,
            'data_conclusao': self.data_conclusao
        }


class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.projetos = []

    def criar_projeto(self, nome, descricao):
        novo_projeto = Projeto(nome, descricao)
        self.projetos.append(novo_projeto)
        return novo_projeto

    def listar_projetos(self):
        return self.projetos
