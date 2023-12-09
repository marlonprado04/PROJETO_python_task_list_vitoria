class Projeto:
    def __init__(self, nome, descricao):
        # Inicializa um novo projeto com um nome e descrição
        self.nome = nome
        self.descricao = descricao
        # Inicializa a lista de tarefas do projeto como vazia
        self.lista_de_tarefas = []

    # Adiciona uma tarefa à lista de tarefas
    def adicionar_tarefa(self, tarefa):
        self.lista_de_tarefas.append(tarefa)

    # Mostra o status geral do projeto
    def mostrar_status_geral_do_projeto(self):
        # Calcula o total de tarefas no projeto
        total_tarefas = len(self.lista_de_tarefas)
        # Conta o número de tarefas pendentes
        tarefas_pendentes = sum(
            1 for tarefa in self.lista_de_tarefas if tarefa.status == "Pendente"
        )

        # Calcula a porcentagem de tarefas pendentes em relação ao total e evita divisão por zero
        porcentagem_tarefas_pendentes = (
            (tarefas_pendentes / total_tarefas) * 100 if total_tarefas > 0 else 0
        )

        # Exibe as informações sobre o status do projeto
        print(f"Total de tarefas: {total_tarefas}")
        print(f"Tarefas pendentes: {tarefas_pendentes}")
        print(f"Porcentagem de tarefas pendentes: {porcentagem_tarefas_pendentes:.2f}%")
