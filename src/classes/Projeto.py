# Importa classe com valores constantes 
from .Tarefa import CONCLUIDA
from .Tarefa import Tarefa

class Projeto:
    # Define ID a ser compartilhado entre todas as instâncias da classe
    _id = 1
    
    # Definindo variáveis da classe
    def __init__(self, titulo, descricao):
        # Atribui um ID único ao projeto
        self.id = Projeto._id
        # Incrementa o contador de IDs
        Projeto._id += 1
        self.titulo = titulo
        self.descricao = descricao
        # Cria lista de tarefas como vazia
        self.id_tarefas = []

    # Adiciona uma tarefa ao projeto
    def adicionar_tarefa(self, titulo, descricao):
        # Cria instância da tarefa e adiciona 
        tarefa = Tarefa(titulo, descricao)
        # Adiciona tarefa ao projeto
        self.id_tarefas.append(tarefa.id)

    # Retorna status do projeto
    def mostrar_status_do_projeto(self):
        # Conta o número de tarefas concluídas
        tarefas_concluidas = sum(1 for id_tarefa in self.id_tarefas if Tarefa.tarefas[id_tarefa].status == CONCLUIDA)
        # Retorna a porcentagem de tarefas concluídas
        if not self.id_tarefas:
            return "O projeto não possui tarefas."
        else:
            percentual_concluido = (tarefas_concluidas / len(self.id_tarefas)) * 100
            return f"Conclusão do projeto: {percentual_concluido:.2f}%"
        
    # Trata os valores da classe para seguirem a estrutura de um arquivo .json
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "id_tarefas": self.id_tarefas,
        }
