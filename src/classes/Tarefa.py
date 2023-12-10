# Importa biblioteca para trabalhar com datas
from datetime import datetime

# Importa classe com valores constantes
from config.Constantes import Constantes


class Tarefa:
    # Define ID a ser compartilhado entre todas as instâncias da classe
    _id_counter = 1

    # Define atributos da classe
    def __init__(self, titulo, descricao, status="Pendente"):
        # Atribui um ID único à tarefa
        self.tarefa_id = Tarefa._id_counter
        # Incrementa o contador de IDs
        Tarefa._id_counter += 1
        self.titulo = titulo
        self.descricao = descricao
        # Recebe o status padrão "pendente" ao criar uma nova tarefa
        self.status = status
        # Recebe a data atual como data de criação
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Demais informações vêm preenchidas como vazias na construção de uma tarefa
        self.data_conclusao = None
        self.projeto = None
        self.usuario_atribuido = None

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

    # Atualiza status e data de conclusão da tarefa dinamicamente
    def atualizar_status(self):
        # Verifica se o status da tarefa está como concluído
        if self.status == Constantes.CONCLUIDA:
            # Atualiza o status da tarefa para pendente
            self.status = Constantes.PENDENTE
            # Atualiza a data de conclusão para vazio
            self.data_conclusao = None
        else:
            # Atualiza o status da tarefa para concluída
            self.status = Constantes.CONCLUIDA
            # Atualiza a data de conclusão para agora
            self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Atribui um projeto à tarefa
    def atribuir_projeto(self, projeto):
        if self.projeto:
            # Se a tarefa já estava associada a um projeto, remova-a desse projeto
            self.projeto.remover_tarefa(self)
        self.projeto = projeto
        projeto.adicionar_tarefa(self)

    # Obtém o projeto associado à tarefa
    def obter_projeto(self):
        return self.projeto

    # Atribui um usuário à tarefa
    def atribuir_usuario(self, usuario):
        if self.usuario_atribuido:
            # Se a tarefa já estava associada a um usuário, remova-a desse usuário
            self.usuario_atribuido.remover_tarefa(self)
        self.usuario_atribuido = usuario
        usuario.adicionar_tarefa(self)

    # Obtém o usuário associado à tarefa
    def obter_usuario(self):
        return self.usuario_atribuido
