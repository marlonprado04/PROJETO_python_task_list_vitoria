# Importa classe com valores constantes 
from Tarefa import CONCLUIDA

class Projeto:
    
    # Definindo variáveis da classe
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        # Cria lista de tarefas como vazia
        self.tarefas = []

    # Adiciona tarefa ao projeto
    def adicionar_tarefa(self, tarefa):
        # Adiciona tarefa ao projeto
        self.tarefas.append(tarefa)

    # Retorna status do projeto
    def mostrar_status_do_projeto(self):
        # Conta o número de tarefas concluídas
        tarefas_concluidas = sum(1 for tarefa in self.tarefas if tarefa.status == CONCLUIDA)
        # Retorna a porcentagem de tarefas concluídas
        if not self.tarefas:
            return "O projeto não possui tarefas."
        else:
            percentual_concluido = (tarefas_concluidas / len(self.tarefas)) * 100
            return f"Conclusão do projeto: {percentual_concluido:.2f}%"
