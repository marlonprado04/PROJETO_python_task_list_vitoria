# Importa biblioteca para trabalhar com datas
from datetime import datetime

from .Database import Database

# Define constantes para os status das tarefas
PENDENTE = "Pendente"
CONCLUIDA = "Concluída"

class Tarefa:
    # Define atributos da classe
    def __init__(self, titulo, status=PENDENTE):
        self.titulo = titulo
        # Recebe o status padrão "pendente" ao criar uma nova tarefa
        self.status = status
        # Recebe a data atual como data de criação
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Demais informações vêm preenchidas como vazias na construção de uma tarefa
        self.id = None
        self.descricao = None
        self.data_conclusao = None
        self.id_projetos = []
        self.id_usuarios  = []
        
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

    # Adiciona um novo projeto no fim da lista se ele não existir
    def adicionar_projeto(self, id):
        # Converte ID em int
        id = int(id)
        
        # Verifica se o id do projeto não está na lista de ID 
        if id not in self.id_projetos:
            # Adiciona o ID do projeto na lista de ID
            self.id_projetos.append(id)
            
    # Renove o projeto na lista de projetos da tarefa
    def remover_projeto(self, id):
        # Converte ID em int
        id = int(id)
        
        # Remove o ID do item 
        self.id_projetos.remove(id)
    
    # Atualiza status e data de conclusão da tarefa dinamicamente
    def atualizar_status(self):
        # Verifica se o status da tarefa está como concluída
        if self.status == CONCLUIDA:
            # Atualiza o status da tarefa para pendente
            self.status = PENDENTE
            # Atualiza a data de conclusão para vazio
            self.data_conclusao = None
        else:
            # Atualiza o status da tarefa para concluída
            self.status = CONCLUIDA
            # Atualiza a data de conclusão para agora
            self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    # Trata os valores da classe para seguirem a estrutura de um arquivo .json
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_criacao": self.data_criacao,
            "data_conclusao": self.data_conclusao,
            "id_projetos": None if self.id_projetos is None else self.id_projetos,
            "id_usuarios": None if self.id_usuarios is None else self.id_usuarios,
        }
    
    # Faz o tratamento dos dados da tarefa para dados legíveis em uma linha
    @classmethod
    def to_line(cls, dados):
        id_str = f"ID: {dados['id']}" if 'id' in dados else "ID: N/A"
        titulo_str = f"Titulo: {dados['titulo']}" if 'titulo' in dados else "Titulo: N/A"
        descricao_str = f"Descrição: {dados['descricao']}" if 'descricao' in dados else "Descrição: N/A"
        data_criacao_str = f"Criada em: {dados['data_criacao']}" if 'data_criacao' in dados else "Criada em: N/A"
        status_str = f"Status: {dados['status']}" if 'status' in dados else "Status: N/A"
        data_conclusao_str = f"Concluída em: {dados['data_conclusao']}" if 'data_conclusao' in dados else "Concluída em: N/A"
        id_usuarios_str = f"ID Usuários: {dados['id_usuarios']}" if 'id_usuarios' in dados else "ID Usuários: N/A"
        id_projetos_str = f"ID Projetos: {dados['id_projetos']}" if 'id_projetos' in dados else "ID Projetos: N/A"

        return f"{id_str} | {titulo_str} | {descricao_str} | {data_criacao_str} | {status_str} | {data_conclusao_str} | {id_projetos_str} | {id_usuarios_str}"

    
    # Cria uma nova instância a partir dos dados de dicionário passados
    @classmethod
    def criar_tarefa_a_partir_de_dict(cls, dados):
        tarefa = cls(dados['titulo'], dados['status'])
        tarefa.id = dados['id']
        tarefa.data_criacao = dados['data_criacao']
        tarefa.descricao = dados['descricao']
        tarefa.data_conclusao = dados['data_conclusao']
        tarefa.id_projetos = dados['id_projetos']
        tarefa.id_usuarios = dados['id_usuarios']
        return tarefa
    