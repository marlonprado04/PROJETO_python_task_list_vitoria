import json

class Tarefa:
    def __init__(self, titulo, descricao, status, data_criacao, data_conclusao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_criacao = data_criacao
        self.data_conclusao = data_conclusao

    def to_dict(self):
        # Converte os atributos da tarefa em um dicionário
        return {
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'data_criacao': self.data_criacao,
            'data_conclusao': self.data_conclusao
        }

    @staticmethod
    def criar_tarefa_from_dict(tarefa_dict):
        # Método auxiliar para criar uma instância de Tarefa a partir de um dicionário
        return Tarefa(
            titulo=tarefa_dict['titulo'],
            descricao=tarefa_dict['descricao'],
            status=tarefa_dict['status'],
            data_criacao=tarefa_dict['data_criacao'],
            data_conclusao=tarefa_dict['data_conclusao']
        )

    @staticmethod
    def salvar_tarefas_em_json(tarefas, caminho_arquivo='data/database.json'):
        # Salva a lista de tarefas em um arquivo JSON
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump([tarefa.to_dict() for tarefa in tarefas], arquivo)

    @staticmethod
    def carregar_tarefas_de_json(caminho_arquivo='data/database.json'):
        # Carrega a lista de tarefas a partir de um arquivo JSON
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                tarefas_dict = json.load(arquivo)
                return [Tarefa.criar_tarefa_from_dict(tarefa) for tarefa in tarefas_dict]
        except FileNotFoundError:
            return []

