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
        # Converte o ID em int
        id = int(id)

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

    # Atualiza o email do usuario
    def atualizar_email(self, novo_email):
        self.email = novo_email

    # Atualiza o nome do usuario
    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome

    # Obtém o email do usuário
    def obter_nome(self):
        return self.nome

    # Obtém o email do usuário
    def obter_email(self):
        return self.email

    # Renove o ID de uma tarefa do usuario
    def remover_tarefa(self, id):
        # Converte ID em int
        id = int(id)

        self.id_tarefas.remove(id)

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
        usuario = cls(dados["nome"])
        usuario.id = dados["id"]
        usuario.email = dados["email"]
        usuario.id_tarefas = dados["id_tarefas"]
        usuario.id_projetos = dados["id_projetos"]
        return usuario

    # Faz o tratamento dos dados do usuário para dados legíveis em uma linha
    @classmethod
    def to_line(cls, dados):
        id_str = f"ID: {dados['id']}" if "id" in dados else "ID: N/A"
        nome_str = f"Nome: {dados['nome']}" if "nome" in dados else "Nome: N/A"
        email_str = f"Email: {dados['email']}" if "email" in dados else "Email: N/A"
        id_tarefas_str = (
            f"ID Tarefas: {dados['id_tarefas']}"
            if "id_tarefas" in dados
            else "ID Tarefas: N/A"
        )
        id_projetos = (
            f"ID Projetos: {dados['id_projetos']}"
            if "id_projetos" in dados
            else "ID Projetos: N/A"
        )

        return f"{id_str} | {nome_str} | {email_str} | {id_tarefas_str} | {id_projetos}"
