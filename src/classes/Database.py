import os
import json
import time

class Database:
    # Inicia a classe informando o nome do arquivo
    def __init__(self, caminho_do_arquivo):
        self.caminho_do_arquivo = caminho_do_arquivo
        self.verificar_ou_criar_arquivo()
        self.dados = self.carregar_json()

    # Verifica existência do arquivo e o cria se não existir
    def verificar_ou_criar_arquivo(self):
        # Extrai o diretório do caminho do arquivo
        diretorio = os.path.dirname(self.caminho_do_arquivo)

        # Verifica se o diretório existe, se não existir, cria
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Verifica se o arquivo existe, se não existir, cria
        if not os.path.exists(self.caminho_do_arquivo):
            # Cria o arquivo com dados padrão
            with open(self.caminho_do_arquivo, 'w') as arquivo:
                json.dump({'usuarios': [], 'projetos': [], 'tarefas': []}, arquivo, indent=4)

    # Carrega dados do arquivo de acordo com o caminho passado
    def carregar_json(self):
        try:
            # Abre o arquivo json a partir do caminho informado na construção do objeto
            with open(self.caminho_do_arquivo, 'r') as arquivo:
                # Armazena leitura dos dados em uma variável
                dados = json.load(arquivo)
            # Retorna variável com os dados lidos
            return dados
        except FileNotFoundError:
            # Se não encontrado, o arquivo é criado em branco
            return {'usuarios': [], 'projetos': [], 'tarefas': []}

    # Atualiza o arquivo 
    def atualizar_json(self):
        # Abre o arquivo passado e atualiza os dados
        with open(self.caminho_do_arquivo, 'w') as file:
            #  Adiciona os dados dentro do arquivo
            json.dump(self.dados, file, indent=4)
        # Recarrega os dados após a atualização
        self.dados = self.carregar_json()

    # Adiciona informações do usuário ao arquivo
    def adicionar_usuario(self, usuario):
        # Define o ID como tamanho da lista + 1 
        usuario.id = len(self.dados["usuarios"]) + 1
        self.dados['usuarios'].append(usuario.to_dict())
        self.atualizar_json()

    # Adiciona informações do projeto ao arquivo
    def adicionar_projeto(self, projeto):
        # Define o ID como tamanho da lista + 1 
        projeto.id = len(self.dados["projetos"]) + 1
        self.dados['projetos'].append(projeto.to_dict())
        self.atualizar_json()

    # Adiciona informações da tarefa ao arquivo
    def adicionar_tarefa(self, tarefa):
        # Define o ID como tamanho da lista + 1 
        tarefa.id = len(self.dados["tarefas"]) + 1
        self.dados['tarefas'].append(tarefa.to_dict())
        self.atualizar_json()

    # Consulta informações da tarefa de acordo com ID
    def consultar_tarefa_por_id(self, id):
        # Para cada tarefa dentro do objeto de tarefas
        for tarefa in self.dados['tarefas']:
            # Retorna a tarefa completa se o ID bater
            if tarefa['id'] == int(id):
                return tarefa
        # Se não, retorna nada
        return "Nenhuma tarefa encontrada."
    
    # Consulta informações do projeto de acordo com ID
    def consultar_projeto_por_id(self, id):
        # Para cada projeto dentro do objeto de projetos
        for projeto in self.dados['projetos']:
            # Retorna o projeto completo se o ID bater
            if projeto['id'] == int(id):
                return projeto
        # Se não, retorna nada
        return "Nenhum projeto encontrado."
    
    # Consultar informações do usuario de acordo com ID
    def consultar_usuario_por_id(self, id):
        # Para cada usuário dentro do objeto de usuários
        for usuario in self.dados['usuarios']:
            # Retorna os dados completos do usuário se o ID bater
            if usuario["id"]== int(id):
                return usuario
        # Se não, retorna que não foi localizado
        return "Nenhum usuário localizado."
    
    # Modifica informações da tarefa no arquivo com base no ID
    def atualizar_tarefa(self, id, dados):
        # Procura pela tarefa com o ID específico
        for tarefa in self.dados['tarefas']:
            if tarefa['id'] == int(id):
                # Atualiza os dados da tarefa existente com os novos dados
                tarefa.update(dados.to_dict())
                self.atualizar_json()
                return "Tarefa atualizada com sucesso!"
        # Se o ID da tarefa não for encontrado, printa uma mensagem
        print(f"Tarefa com ID {id} não encontrada.")
        
    # Modifica informações do projeto no arquivo com base no ID
    def atualizar_projeto(self, id, dados):
        # Procura pelo projeto com o ID específico
        for projeto in self.dados['projetos']:
            if projeto['id'] == int(id):
                # Atualiza os dados existentes com os novos dados
                projeto.update(dados.to_dict())
                self.atualizar_json()
                return "Projeto atualizado com sucesso"
        # Se o ID do projeto não for encontrado, printa uma mensagem
        print(f"Projeto com ID {id} não encontrada.")
        
    # Modifica informações do usuário no arquivo com base no ID
    def atualizar_usuario(self, id, dados):
        # Procura pelo usuário com o ID específico
        for usuario in self.dados['usuarios']:
            if usuario['id'] == int(id):
                # Atualiza os dados existentes com os novos dados
                usuario.update(dados.to_dict())
                self.atualizar_json()
                return "Usuário atualizado com sucesso"
        # Se o ID do usuário não for encontrado, printa uma mensagem
        print(f"Usuário com ID {id} não encontrada.")
        
    # Lista todas as tarefas cadastradas
    def listar_tarefas(self):
        # Cria variável para armazenar lista de tarefas
        lista_de_tarefas = []
        # Verifica se existem tarefas dentro do json
        if len(self.dados["tarefas"]) > 0:
            # Adiciona cada tarefa dentro do json na lista de tarefas
            for tarefa in self.dados["tarefas"]:
                lista_de_tarefas.append(tarefa)
            # Retorna lista de tarefas prenchida
            return lista_de_tarefas
        # Caso esteja vazio, retorna que nenhuma tarefa foi localizada
        return "Nenhuma tarefa localizada"
    
    # Exclui a tarefa do arquivo com base no ID
    def excluir_tarefa(self, id):
        # Procura pela tarefa com o ID específico
        for indice, tarefa in enumerate(self.dados['tarefas']):
            if tarefa['id'] == int(id):
                # Remove a tarefa da lista
                del self.dados['tarefas'][indice]
                self.atualizar_json()
                print(f"Tarefa com ID {id} excluída com sucesso.")
                return
        # Se o ID da tarefa não for encontrado, printa uma mensagem
        print(f"Tarefa com ID {id} não encontrada.")
