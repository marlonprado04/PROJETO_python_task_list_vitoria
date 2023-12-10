# Importa classe com valores constantes 
from .Tarefa import CONCLUIDA
from .Tarefa import Tarefa

class Projeto:
    # Define ID a ser compartilhado entre todas as instâncias da classe
    _id = 1
    
    # Definindo variáveis da classe
    def __init__(self, titulo):
        # Atribui um ID único ao projeto
        self.id = Projeto._id
        # Incrementa o contador de IDs
        Projeto._id += 1
        self.titulo = titulo
        self.descricao = None
        # Cria lista de tarefas como vazia
        self.id_tarefas = []
        self.id_usuarios = []

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
