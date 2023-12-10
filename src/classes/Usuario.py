from Tarefa import Tarefa

class Usuario:
    # Definindo estrutura da classe
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        # Inicializa a lista de tarefas atribuídas como vazia
        self.tarefas_atribuidas = []

    # Adiciona tarefa na lista de tarefas atribuídas ao usuário
    def atribuir_tarefa(self, titulo, descricao):
        # Cria uma nova instância de Tarefa
        nova_tarefa = Tarefa(titulo, descricao)
        # Adiciona a tarefa instanciada na lista de tarefas atribuídas
        self.tarefas_atribuidas.append(nova_tarefa)

    # Lista tarefas do usuário
    def listar_tarefas_atribuidas(self):
        # Verifica se usuário não possui tarefas atribuídas e imprime mensagem
        if not self.tarefas_atribuidas:
            return "O usuário não possui tarefas atribuídas."

        # Cria variável e armazena uma lista com as tarefas
        lista_tarefas = "\n".join(
            [
                f"Título: {tarefa.obter_titulo()}, Descrição: {tarefa.obter_descricao()}, Status: {tarefa.status}"
                for tarefa in self.tarefas_atribuidas
            ]
        )

        # Retorna a lista de tarefas atribuídas ao usuário
        return f"Tarefas atribuídas ao usuário {self.nome}:\n{lista_tarefas}"

    # Atualiza o status da tarefa
    def atualizar_status(self, tarefa):
        # Marca a tarefa como concluída (usando o método na classe Tarefa)
        tarefa.atualizar_status()