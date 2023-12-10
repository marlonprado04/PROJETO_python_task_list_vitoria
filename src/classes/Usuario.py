from .Tarefa import Tarefa

class Usuario:
    
    # Definindo estrutura da classe
    def __init__(self, nome):
        self.nome = nome
        # Inicializa os demais campos vazios
        self.id = None
        self.email = None
        self.id_tarefas = []
        self.id_projetos = []

    # Adiciona tarefa na lista de tarefas atribuídas ao usuário
    def adicionar_tarefa(self, id):
        # Adiciona a tarefa instanciada na lista de tarefas atribuídas
        self.id_tarefas.append(id)

    # Lista tarefas do usuário
    def listar_tarefas_atribuidas(self):
        # Verifica se usuário não possui tarefas atribuídas e imprime mensagem
        if not self.id_tarefas:
            return "O usuário não possui tarefas atribuídas."
        
        lista_de_tarefas = []
        # Intera sobre todos os IDs de tarefa atribuídas
        for id in self.id_tarefas:
            lista_de_tarefas.append(f"ID: {id}, Título: {Tarefa[id].obter_titulo()}")
            
        # Concatena as strings em uma única mensagem
        lista_de_tarefas_str = "\n".join(lista_de_tarefas)

        # Retorna a lista de tarefas atribuídas ao usuário
        return f"Tarefas atribuídas ao usuário {self.nome}:\n{lista_de_tarefas_str}"

    # Atualiza o status da tarefa
    def atualizar_status(self, id):
        # Atualiza o status da tarefa com o ID passado
        Tarefa[id].atualizar_status()

    # Trata os valores da classe para seguirem a estrutura de um arquivo .json
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "id_tarefas": self.id_tarefas,
            "id_projetos": self.id_projetos,
        }

     # Cria método da classe para criar uma nova instância a partir dos dados de dicionário passados
    @classmethod
    def criar_usuario_a_partir_de_dict(cls, dados):
        usuario = cls(dados['nome'])
        usuario.id = dados["id"]
        usuario.email = dados['email']
        usuario.id_tarefas = dados["id_tarefas"]
        usuario.id_projetos = dados["id_projetos"]
        return usuario