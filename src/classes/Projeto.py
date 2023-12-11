# Importa classe com valores constantes 
from .Tarefa import CONCLUIDA
from .Tarefa import Tarefa

class Projeto:
    # Definindo variáveis da classe
    def __init__(self, titulo):
        self.titulo = titulo
        self.descricao = None
        # Cria lista de tarefas como vazia
        self.id = None
        self.id_tarefas = []
        self.id_usuarios = []

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

    # Adiciona o ID de uma tarefa ao projeto
    def adicionar_tarefa(self, id_tarefa):
        # Cria instância da tarefa e adiciona 
        self.id_tarefas.append(id_tarefa)

    # Retorna status do projeto
    def mostrar_status_do_projeto(self):
        # Verifica se não existem tarefa do projeto
        if not self.id_tarefas:
            return "O projeto não possui tarefas."
        else:
            # Conta o número de tarefas concluídas
            tarefas_concluidas = sum(1 for id in self.id_tarefas if Tarefa[id].status == CONCLUIDA)
            # Armazena o valor percentual de tarefas com status de concluídas
            percentual_concluido = (tarefas_concluidas / len(self.id_tarefas)) * 100
            # Retorna mensagem com percentual de conclusão
            return f"Conclusão do projeto: {percentual_concluido:.2f}%"
        
    # Trata os valores da classe para seguirem a estrutura de um arquivo .json
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "id_tarefas": self.id_tarefas,
            "id_usuarios": self.id_usuarios
        }

    # Cria método da classe para criar uma nova instância a partir dos dados de dicionário passados
    @classmethod
    def criar_projeto_a_partir_de_dict(cls, dados):
        projeto = cls(dados['titulo'])
        projeto.descricao = dados["descricao"]
        projeto.id = dados['id']
        projeto.id_tarefas = dados["id_tarefas"]
        projeto.id_usuarios = dados["id_usuarios"]
        return projeto
    
    
    # Faz o tratamento dos dados do projeto para dados legíveis em uma linha
    @classmethod
    def to_line(cls, dados):
        id_str = f"ID: {dados['id']}" if 'id' in dados else "ID: N/A"
        titulo_str = f"Titulo: {dados['titulo']}" if 'titulo' in dados else "Titulo: N/A"
        descricao_str = f"Descrição: {dados['descricao']}" if 'descricao' in dados else "Descrição: N/A"
        id_tarefas_str = f"ID Tarefas: {dados['id_tarefas']}" if 'id_tarefas' in dados else "ID Tarefas: N/A"
        id_usuarios_str = f"ID Usuários: {dados['id_usuarios']}" if 'id_usuarios' in dados else "ID Usuários: N/A"
        
        return f"{id_str} | {titulo_str} | {descricao_str} | {id_tarefas_str} | {id_usuarios_str}"
