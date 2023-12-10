# Importa biblioteca para trabalhar com datas
from datetime import datetime

from .Database import Database

# Define constantes para os status das tarefas
PENDENTE = "Pendente"
CONCLUIDA = "Concluída"

class Tarefa:
    # Define atributos da classe
    def __init__(self, titulo, status=PENDENTE):
        self.titulo = titulo
        # Recebe o status padrão "pendente" ao criar uma nova tarefa
        self.status = status
        # Recebe a data atual como data de criação
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Demais informações vêm preenchidas como vazias na construção de uma tarefa
        self.id = None
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
        # Verifica se o status da tarefa está como concluída
        if self.status == CONCLUIDA:
            # Atualiza o status da tarefa para pendente
            self.status = PENDENTE
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
    
    # Cria método da classe para criar uma nova instância a partir dos dados de dicionário passados
    @classmethod
    def criar_tarefa_a_partir_de_dict(cls, dados_tarefa):
        tarefa = cls(dados_tarefa['titulo'], dados_tarefa['status'])
        tarefa.id = dados_tarefa['id']
        tarefa.data_criacao = dados_tarefa['data_criacao']
        tarefa.descricao = dados_tarefa['descricao']
        tarefa.data_conclusao = dados_tarefa['data_conclusao']
        tarefa.id_projetos = dados_tarefa['id_projetos']
        tarefa.id_usuarios = dados_tarefa['id_usuarios']
        return tarefa