import os
import json


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
            with open(self.caminho_do_arquivo, "w") as arquivo:
                json.dump(
                    {"usuarios": [], "projetos": [], "tarefas": []}, arquivo, indent=4
                )

    # Carrega dados do arquivo de acordo com o caminho passado
    def carregar_json(self):
        try:
            # Abre o arquivo json a partir do caminho informado na construção do objeto
            with open(self.caminho_do_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
                # Verifica se o arquivo está vazio
                if not conteudo:
                    # Retorna a estrutura básica do arquivo, caso esteja vazio
                    return {"usuarios": [], "projetos": [], "tarefas": []}
                # Senão, retorna o arquivo lido
                return json.loads(conteudo)
        except FileNotFoundError:
            # Se não encontrado, o arquivo é criado em branco
            return {"usuarios": [], "projetos": [], "tarefas": []}

    # Atualiza o arquivo
    def atualizar_json(self):
        # Abre o arquivo passado e atualiza os dados
        with open(self.caminho_do_arquivo, "w") as file:
            #  Adiciona os dados dentro do arquivo
            json.dump(self.dados, file, ensure_ascii=False, indent=4)
        # Recarrega os dados após a atualização
        self.dados = self.carregar_json()

    # ------- OPERAÇÕES COM TAREFAS -------

    # Adiciona informações da tarefa ao arquivo
    def adicionar_tarefa(self, tarefa):
        # Define o ID como tamanho da lista + 1
        tarefa.id = len(self.dados["tarefas"]) + 1
        self.dados["tarefas"].append(tarefa.to_dict())
        self.atualizar_json()
        return "Tarefa adicionada com sucesso"

    # Modifica informações da tarefa no arquivo com base no ID
    def atualizar_tarefa(self, id, dados):
        # Procura pela tarefa com o ID específico
        for tarefa in self.dados["tarefas"]:
            if tarefa["id"] == int(id):
                # Atualiza os dados da tarefa existente com os novos dados
                tarefa.update(dados.to_dict())
                self.atualizar_json()
                return "Tarefa atualizada com sucesso!"
        # Se o ID da tarefa não for encontrado, printa uma mensagem
        print(f"Tarefa com ID {id} não encontrada.")

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
        return []

    # Exclui a tarefa do arquivo com base no ID
    def excluir_tarefa(self, id):
        # Converte o ID em int
        id = int(id)

        # Procura pela tarefa com o ID específico
        for indice, tarefa in enumerate(self.dados["tarefas"]):
            if tarefa["id"] == id:
                # Remove a tarefa da lista
                del self.dados["tarefas"][indice]
                self.atualizar_json()
                print(f"Tarefa com ID {id} excluída com sucesso.")
                return
        # Se o ID da tarefa não for encontrado, printa uma mensagem
        print(f"Tarefa com ID {id} não encontrada.")

    # Consulta informações da tarefa de acordo com ID
    def consultar_tarefa_por_id(self, id):
        # Para cada tarefa dentro do objeto de tarefas
        for tarefa in self.dados["tarefas"]:
            # Retorna a tarefa completa se o ID bater
            if tarefa["id"] == int(id):
                return tarefa
        # Se não, retorna nada
        return "Nenhuma tarefa encontrada."

    # ------- OPERAÇÕES COM PROJETOS -------

    # Adiciona informações do projeto ao arquivo
    def adicionar_projeto(self, projeto):
        # Define o ID como tamanho da lista + 1
        projeto.id = len(self.dados["projetos"]) + 1
        self.dados["projetos"].append(projeto.to_dict())
        self.atualizar_json()
        return "Projeto adicionado com sucesso"

    # Lista todos os projetos
    def listar_projetos(self):
        # Cria variável para armazenar lista de projetos
        lista_de_projetos = []
        # Verifica se existem projetos dentro do json
        if len(self.dados["projetos"]) > 0:
            # Adiciona cada projeto dentro do json na lista de projetos
            for projeto in self.dados["projetos"]:
                lista_de_projetos.append(projeto)
            # Retorna lista de projetos prenchida
            return lista_de_projetos
        # Caso esteja vazio, retorna que nenhum projeto foi localizado
        return []

    # Modifica informações do projeto no arquivo com base no ID
    def atualizar_projeto(self, id, dados):
        # Procura pelo projeto com o ID específico
        for projeto in self.dados["projetos"]:
            if projeto["id"] == int(id):
                # Atualiza os dados existentes com os novos dados
                projeto.update(dados.to_dict())
                self.atualizar_json()
                return "Projeto atualizado com sucesso"
        # Se o ID do projeto não for encontrado, printa uma mensagem
        print(f"Projeto com ID {id} não encontrada.")

    # Exclui o projeto do arquivo com base no ID fornecido
    def excluir_projeto(self, id):
        # Converte o ID pra int
        id = int(id)

        # Procura pelo projeto com o ID específico
        for indice, projeto in enumerate(self.dados["projetos"]):
            if projeto["id"] == id:
                # Remove a tarefa da lista
                del self.dados["projetos"][indice]
                self.atualizar_json()
                print(f"Projeto com ID {id} excluído com sucesso.")
                return
        # Se o ID do projeto não for encontrado, printa uma mensagem
        print(f"Projeto com ID {id} não encontrada.")

    # Consulta informações do projeto de acordo com ID
    def consultar_projeto_por_id(self, id):
        # Para cada projeto dentro do objeto de projetos
        for projeto in self.dados["projetos"]:
            # Retorna o projeto completo se o ID bater
            if projeto["id"] == int(id):
                return projeto
        # Se não, retorna nada
        return "Nenhum projeto encontrado."

    # Lista as tarefas que não fazem parte do projeto
    def listar_tarefas_dentro_do_projeto(self, id):
        # Converte o ID recebido em int
        id = int(id)

        # Obtém o projeto correspondente ao ID
        projeto = self.consultar_projeto_por_id(id)

        # Cria lista para armazenar os IDs
        lista_de_tarefas = []

        # Verifica se o tamanho da lista de tarefas do projeto é maior que zero
        if len(projeto["id_tarefas"]) > 0:
            # Mapeia todos os IDs dentro do array de ID de tarefas
            for id_tarefa in projeto["id_tarefas"]:
                # Adiciona a tarefa pesquisada pelo ID
                lista_de_tarefas.append(self.consultar_tarefa_por_id(id_tarefa))

            # Retorna a lista de tarefas
            return lista_de_tarefas

        # Retorna lista vazia
        return []

    # Lista as tarefas que fazem parte do projeto
    def listar_tarefas_fora_do_projeto(self, id):
        # Converte o ID recebido em int
        id = int(id)

        # Obtém a lista completa de tarefas
        todas_tarefas = self.listar_tarefas()

        # Cria lista para armazenar tarefas sem o projeto vinculado
        tarefas_fora_do_projeto = []

        # Verifica todas as tarefas da lista
        for tarefa in todas_tarefas:
            # Verifica se o ID do projeto não está na lista de IDs de projetos na tarefa
            if id not in tarefa["id_projetos"]:
                # Armazena a tarefa dentro da lista de tarefas fora do projeto
                tarefas_fora_do_projeto.append(tarefa)

        # Retorna a lista de tarefas que não estão no projeto
        return tarefas_fora_do_projeto

    # ------- OPERAÇÕES COM USUÁRIOS -------

    # Adiciona informações do usuário ao arquivo
    def adicionar_usuario(self, usuario):
        # Define o ID como tamanho da lista + 1
        usuario.id = len(self.dados["usuarios"]) + 1
        self.dados["usuarios"].append(usuario.to_dict())
        self.atualizar_json()
        return "Usuário adicionado com sucesso"

    # Modifica informações do usuário no arquivo com base no ID
    def atualizar_usuario(self, id, dados):
        # Procura pelo usuário com o ID específico
        for usuario in self.dados["usuarios"]:
            if usuario["id"] == int(id):
                # Atualiza os dados existentes com os novos dados
                usuario.update(dados.to_dict())
                self.atualizar_json()
                return "Usuário atualizado com sucesso"
        # Se o ID do usuário não for encontrado, printa uma mensagem
        print(f"Usuário com ID {id} não encontrada.")

    # Exclui o usuário do arquivo com base no ID fornecido
    def excluir_usuario(self, id):
        # Converte o ID pra int
        id = int(id)

        # Procura pelo usuário com o ID específico
        for indice, usuario in enumerate(self.dados["usuarios"]):
            if usuario["id"] == id:
                # Remove o usuário da lista
                del self.dados["usuarios"][indice]
                self.atualizar_json()
                print(f"Usuário com ID {id} excluído com sucesso.")
                return
        # Se o ID do usuário não for encontrado, printa uma mensagem
        print(f"Usuário com ID {id} não encontrado.")

    # Lista todos os usuários cadastrados
    def listar_usuarios(self):
        # Cria variável para armazenar lista de usuários
        lista_de_usuarios = []

        # Verifica se existem usuários dentro do JSON
        if len(self.dados["usuarios"]) > 0:
            # Adiciona cada usuário dentro do JSON na lista de usuários
            for usuario in self.dados["usuarios"]:
                lista_de_usuarios.append(usuario)

            # Retorna a lista de usuários preenchida
            return lista_de_usuarios

        # Caso esteja vazia, retorna lista vazia
        return []

    # Consultar informações do usuario de acordo com ID
    def consultar_usuario_por_id(self, id):
        # Para cada usuário dentro do objeto de usuários
        for usuario in self.dados["usuarios"]:
            # Retorna os dados completos do usuário se o ID bater
            if usuario["id"] == int(id):
                return usuario
        # Se não, retorna que não foi localizado
        return "Nenhum usuário localizado."

    # Lista as tarefas que fazem parte do usuário
    def listar_tarefas_fora_do_usuario(self, id):
        # Converte o ID recebido em int
        id = int(id)

        # Obtém a lista completa de tarefas
        todas_tarefas = self.listar_tarefas()

        # Cria lista para armazenar tarefas sem o usuário vinculado
        tarefas_fora_do_usuario = []

        # Verifica todas as tarefas da lista
        for tarefa in todas_tarefas:
            # Verifica se o ID do usuário não está na lista de IDs de usuários na tarefa
            if id not in tarefa["id_usuarios"]:
                # Armazena a tarefa dentro da lista de tarefas fora do usuário
                tarefas_fora_do_usuario.append(tarefa)

        # Retorna a lista de tarefas que não estão no usuário
        return tarefas_fora_do_usuario

    # Lista as tarefas que não fazem parte do usuário
    def listar_tarefas_do_usuario(self, id):
        # Converte o ID recebido em int
        id = int(id)

        # Obtém o usuário correspondente ao ID
        usuario = self.consultar_usuario_por_id(id)

        # Cria lista para armazenar os IDs
        lista_de_tarefas = []

        # Verifica se o tamanho da lista de tarefas do usuário é maior que zero
        if len(usuario["id_tarefas"]) > 0:
            # Mapeia todos os IDs dentro do array de ID de tarefas
            for id_tarefa in usuario["id_tarefas"]:
                # Adiciona a tarefa pesquisada pelo ID
                lista_de_tarefas.append(self.consultar_tarefa_por_id(id_tarefa))

            # Retorna a lista de tarefas
            return lista_de_tarefas

        # Retorna lista vazia
        return []
