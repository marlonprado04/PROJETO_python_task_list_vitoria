# Importa classe com valores constantes 
from Constantes import Constantes

class Projeto:
    
    # Definindo variáveis da classe
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        # Cria lista de tarefas como vazia
        self.tarefas = []
        self.total_tarefas = len(self.tarefas)

    # Adiciona tarefa ao projeto
    def adicionar_tarefa(self, tarefa):
        # Adiciona tarefa ao projeto
        self.tarefas.append(tarefa)
        # Atualiza o total de tarefas na classe
        self.total_tarefas = len(self.tarefas)

    # Retorna status do projeto
    def mostrar_status_do_projeto(self):
        # Conta o número de tarefas com status de Concluída
        tarefas_concluidas = sum(
            1 for tarefa in self.tarefas if tarefa.status == Constantes.CONCLUIDA
        )
        # Retorna mensagem com conclusão do projeto
        return f"Conclusão do projeto: {tarefas_concluidas}/{self.total_tarefas}"

