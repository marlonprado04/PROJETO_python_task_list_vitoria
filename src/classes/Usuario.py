from Tarefa import Tarefa

class Usuario:
    
    # Define ID a ser compartilhado entre todas as instâncias da classe
    _id = 1
    
    # Definindo estrutura da classe
    def __init__(self, nome, email, database):
        # Atribui um ID único ao usuário
        self.tarefa_id = Usuario._id
        self.nome = nome
        self.email = email
        # Inicializa a lista de tarefas atribuídas como vazia
        self.tarefas_atribuidas = []
        # Mantém uma referência à instância de Database
        self.database = database

    # Adiciona tarefa na lista de tarefas atribuídas ao usuário
    def criar_tarefa(self, titulo, descricao):
        # Cria uma nova instância de Tarefa
        nova_tarefa = Tarefa(titulo, descricao)
        # Adiciona a tarefa instanciada na lista de tarefas atribuídas
        self.tarefas_atribuidas.append(nova_tarefa.tarefa_id)
        # Salva os dados no arquivo JSON
        self.database.adicionar_tarefa(nova_tarefa.to_dict())

    # Adiciona uma tarefa já existente na lista de tarefas atribuídas ao usuário
    def atribuir_tarefa(self, id_tarefa):
        self.tarefas_atribuidas.append(id_tarefa)
        # Salva os dados no arquivo JSON
        self.database.atualizar_usuario(self.to_dict())

    # Lista tarefas do usuário
    def listar_tarefas_atribuidas(self):
        # Verifica se usuário não possui tarefas atribuídas e imprime mensagem
        if not self.tarefas_atribuidas:
            return "O usuário não possui tarefas atribuídas."

        # Cria variável para armazenar as strings formatadas das tarefas
        lista_tarefas = []

        # Intera sobre todos os IDs de tarefa atribuídas
        for id_tarefa in self.tarefas_atribuidas:
            tarefa = self.database.obter_tarefa_por_id(id_tarefa)
            if tarefa:
                lista_tarefas.append(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}")

        # Concatena as strings em uma única mensagem
        lista_tarefas_str = "\n".join(lista_tarefas)

        # Retorna a lista de tarefas atribuídas ao usuário
        return f"Tarefas atribuídas ao usuário {self.nome}:\n{lista_tarefas_str}"

    # Atualiza o status da tarefa
    def atualizar_status(self, id_tarefa):
        tarefa = self.database.obter_tarefa_por_id(id_tarefa)
        if tarefa:
            # Marca a tarefa como concluída
            tarefa["status"] = "Concluída"
            # Salva os dados no arquivo JSON
            self.database.atualizar_tarefa(tarefa)
