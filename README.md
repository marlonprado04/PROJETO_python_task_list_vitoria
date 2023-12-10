# Lista de tarefas em Python

Projeto de Task List implementado para Vitória Batista da DINFO

O objetivo deste projeto é criar uma ferramenta para gerenciar Usuários, Projetos e Tarefas.

## Enunciado

O enunciado se encontra [neste link](./.docs/escopo.jpeg) e abaixo:

**OBJETIVO:**

Você deverá implementar um Sistema de Gerenciamento de Tarefas utilizando os conceitos vistos até aqui sobre Programação Orientada a Objetos.

**DESCRIÇÃO:**

Você deve criar um sistema de gerenciamento de tarefas que permita aos usuários criar, atribuir e acompanhar o progresso de várias tarefas. Seu sistema deve incluir no mínimo
as seguintes classes:

- **Tarefa:** Representa uma tarefa individual.
  - Deve ter atributos para armazenar detalhes como título, descrição, status e datas de criação e conclusão.
  - Deve ter métodos para alterar o status da tarefa, atualizar a descrição, etc.

- **Usuário:** Representa um usuário do sistema.
  - Deve ter atributos para armazenar detalhes como nome, email e uma lista de tarefas atribuídas ao usuário.
  - Deve ter métodos para criar uma nova tarefa, marcar uma tarefa como concluída, etc.

- **Projeto:** Representa um projeto, que é uma coleção de tarefas.
  - Deve ter atributos para armazenar detalhes como nome, descrição e uma lista de todas as tarefas no
projeto.
  - Deve ter métodos para adicionar uma nova tarefa ao projeto, obter o status geral do projeto, etc.
  - Além disso, seu sistema deve ser capaz de manter os dados. Para isso, você deve implementar funcionalidades para salvar e carregar os dados do seu sistema em um arquivo
JSON.

**Requisitos Adicionais:**

- Seu código deve demonstrar o uso adequado dos conceitos de POO, como encapsulamento, herança.
- Seu código deve ser bem organizado e fácil de ler, com nomes de variáveis descritivos e comentários explicando o código onde necessário.

**Data de Entrega:** 12/dezembro

**Critérios de Avaliação:** Você será avaliado com base na funcionalidade do seu sistema, no uso adequado dos conceitos de POO e na organização e legibilidade do seu código.

## O fluxo do sistema

- Sistema: pergunta se o usuário deseja verificar a lista de TAREFAS, PROJETOS ou USUÁRIOS:
  - Usuário: seleciona a LISTA DE TAREFAS:
    - Sistema: Imprime na tela a lista com todas as tarefas contendo nome, descrição, data de criação, status, data de conclusão, projeto e usuário atribuído
    - Sistema: Apresenta ao usuário as opções de:
      - Selecionar uma tarefa:
        - Usuário: Seleciona uma tarefa:
          - Sistema: Lista as opções para a tarefa selecionada:
            - Atualizar nome ou descrição da tarefa
            - Concluir tarefa
            - Atribuir tarefa a um usuário
            - Atribuir tarefa a um projeto
            - Retornar ao menu anterior
            - Encerrar sistema
      - Selecionar voltar
        - Sistema: retorna ao menu anterior
      - Selecionar encerrar o sistema
        - Encerra na hora
  - Usuário: seleciona LISTA DE PROJETOS:
    - Sistema: Imprime a lista de projetos contendo nome, número de tarefas pendente, número de tarefas total, percentual de conclusão
    - Sistema: apresenta ao usuário as opções de:
      - Selecionar um projeto:
        - Usuário seleciona um projeto:
          - Sistema: lista as opções para o projeto selecionado
            - Atualizar nome e descrição do projeto
            - Listar tarefas do projeto
            - Excluir projeto
      - Selecionar voltar
        - Sistema: retorna ao menu anterior
      - Selecionar encerrar o sistema
        - Encerra na hora
  - Usuário: seleciona LISTA DE USUÁRIOS:
    - Sistema: Imprime na tela a lista com os nomes e emails dos usuários
      - Sistema: apresenta ao usuário as opções de:
        - Selecionar um usuário
          - Usuário: seleciona um usuário:
            - Atualizar nome e email do usuário
            - Listar tarefas atribuídas ao usuário (todos os campos + projeto em que se encontra)
            - Retornar ao menu anterior
            - Encerrar o sistema
        - Selecionar voltar
          - Sistema: retorna ao menu anterior
        - Selecionar encerrar o sistema
          - Encerra na hora

## Lista de métodos (UML)

Tarefas:

  - Listar tarefas
  - Atualizar nome
  - Atualizar descrição
  - Concluir tarefa
  - Atribuir tarefa a um usuário
  - Atribuir tarefa a um projeto
  - Excluir tarefa

Projetos:

  - Listar projetos
  - Atualizar nome
  - Atualizar descrição
  - Listar tarefas do projeto
  - Excluir projeto

Usuários:

  - Listar usuários
  - Atualizar nome
  - Atualizar email
  - Listar tarefas atribuídas
  - Excluir usuário
