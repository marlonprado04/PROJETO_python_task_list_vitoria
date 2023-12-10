# Importa biblioteca para trabalhar com datas
from datetime import datetime

# Define constantes para os status das tarefas
PENDENTE = "Pendente"
CONCLUIDA = "Concluída"

class Tarefa:
    # Define ID a ser compartilhado entre todas as instâncias da classe
    _id = 1

    # Define atributos da classe
    def __init__(self, titulo, status=PENDENTE):
        # Atribui um ID único à tarefa
        self.id = Tarefa._id
        # Incrementa o contador de IDs
        Tarefa._id += 1
        self.titulo = titulo
        # Recebe o status padrão "pendente" ao criar uma nova tarefa
        self.status = status
        # Recebe a data atual como data de criação
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Demais informações vêm preenchidas como vazias na construção de uma tarefa
        self.descricao = None
        self.data_conclusao = None
        self.id_projetos = []
        self.id_usuarios  = []

    # Atualiza o título de acordo com valor passado
    def atualizar_titulo(self, novo_nome):
        self.titulo = novo_nome

    # Obtém valor do título
    def obter_titulo(self):
        return self.titulo

    # Atualiza a descrição de acordo com valor passado
    def atualizar_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    # Obtém valor da descrição
    def obter_descricao(self):
        return self.descricao

    # Atualiza status e data de conclusão da tarefa dinamicamente
    def atualizar_status(self):
        # Verifica se o status da tarefa está como concluído
        if self.status == PENDENTE:
            # Atualiza o status da tarefa para pendente
            self.status = CONCLUIDA
            # Atualiza a data de conclusão para vazio
            self.data_conclusao = None
        else:
            # Atualiza o status da tarefa para concluída
            self.status = CONCLUIDA
            # Atualiza a data de conclusão para agora
            self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Trata os valores da classe para seguirem a estrutura de um arquivo .json
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_criacao": self.data_criacao,
            "data_conclusao": self.data_conclusao,
            "id_projetos": None if self.id_projetos is None else self.id_projetos,
            "id_usuarios": None if self.id_usuarios is None else self.id_usuarios,
        }
