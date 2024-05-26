# gerenciador_de_projetos_e_tarefas
Projeto para criar um sistema de gerenciamento de Clientes, Projetos e Tarefas

# Desafio Técnico

 - dev: [Enio Farias](mailto:eniodefarias@gmail.com)
 - data: 23/05/2024
 - repo: [github/gerenciador_de_projetos_e_tarefas](https://github.com/eniodefarias/gerenciador_de_projetos_e_tarefas)
 

# Proposta:

## Descrição:

Você foi contratado pela empresa Microsoft para desenvolver a nova plataforma
de gestão de projetos e desenvolvimento de software. O sistema legado é
desktop e não atende mais às necessidades da empresa, visto que, em épocas
de COVID-19 os colaboradores e clientes precisam acessar a plataforma pela
internet.

O sistema consiste em gerenciar os projetos da empresa, visando o
planejamento e acompanhamento dos times, projetos, clientes, tarefas, entre
outros.

Os cadastros básicos são (deve-se criar outros a seu critério):
 - o Clientes;
 - o Projetos;
 - o Atividades.

O sistema deve ser capaz de, a qualquer momento, adicionar atividades para
um cliente em seu respectivo projeto. Ao cadastrar as atividades, deve-se
relacionar para qual cliente em qual o projeto.

Deve existir uma tela que lista os projetos em aberto (tratar status dos projetos),
mostrando a qual cliente ele pertence, e com possibilidade de abrir a lista de
atividades que está cadastrada a este projeto.

## Critérios:

 - A interpretação faz parte do projeto;
 - Ao final, postar no GitHub num repositório privado e enviar o e-mail para
xyz@mail.com;
 - Será avaliado a arquitetura do Back-end e Front-end;
 - Será avaliado a qualidade e limpeza do código;
 - Será avaliado a qualidade das telas e organização do Javascript;
 - Testes unitários são obrigatórios;
 - O trabalho deve ser entregue em 96 horas;
 - Back-end da aplicação deve ser com ~~Java e Spring Boot;~~ ‼️ 💡 use Python e Flask
 - Os registros devem ser persistidos com mapeado ORM utilizando o ~~Hibernate em um banco de dados postgres;~~ ‼️ 💡 use SqlAlchemy e Postgres
 - Front-end em VueJs; -> ⁉️ 💡 ou um front simples
 - O sistema deve ter 80% de cobertura de testes unitários na camada de regra de negócio;
 - Criar um diagrama de classe com as entidades do projeto.


# estudo de caso

## Tabelas:

### Usuários

 - cadastro de usuários:
   - no primeiro uso, ter um usuário ADMIN e exigir troca de senha
   - somente ADMIN e Gerente pode cadastrar Usuários e Clientes
   - usuários:
     - ADMIN
       - User:
         - criar/modificar/deletar: ADMIN, Gerente, Supervisor, Operador
     - Gerente: Cliente -> Projeto -> Atividade -> Tarefa
       - User: 
         - criar: Gerente, Supervisor, Operador
         - modificar/deletar: Supervisor, Operador
     - Supervisor: Projeto -> Atividade -> Tarefa
       - User:
         - criar/modificar: Operador
     - Operador: Atividade -> Tarefa


 - Usuários:
   - definir em quais clientes podem atuar
     - se selecionado "Cliente" terá acesso a todos os projetos
     - se selecionado "Projeto", terá acesso somente as Atividades do projeto
     - ~~se aplica somente aos grupos "Supervisor" e "Operador"~~
       -  ~~_<small>Vou aplicar aqui o bom senso de que os indívudos do grupo "Gerente" sejam profissionalmente capacitados para saberem se comportar eticamente. Caso ocorram infantilidades nesse ponto, então a gestão de pessoas e recursos humanos podem iniciar um grande projeto de reciclagem profissional com uma analise piscotécnica mais apurada a fim de aprimorar e qualificar seus profissionais.</small>_~~



 - tabela_usuario
   - id_user|id_grupo|email_usuario|nome_usuario|senha_usuario
   - ⚠️ **email_usuario -> deve ser unico**
     - 1|1|ADMIN@localhost|ADMIN|ADMIN
       - deve ser alterado no primeiro login
 

 
- tabela_grupo
   - id_grupo|descr_grupo
     - -> grupo:
       - 1|ADMIN
       - 2|Gerente
       - 3|Supervisor
       - 4|Operador

   
- tabela_cargo
  - id_cargo|descr_cargo
    - apenas para formalidades



- tabela_equipe
  - id_equipe|descr_equipe



 - tabela_times
   - id_time|id_equipe|id_user|id_cargo


### Clientes

 - tabela_cliente
   - id_cliente|nome_cliente

### Projetos

 - tabela_projeto
   - id_projeto|nome_projeto|id_cliente|id_notificacao

 - tabela_projeto_cronograma
   - id_crono_projeto|id_projeto|data_inicial|data_limite|data_fechamento|id_status
 
 - tabela_projeto_usuarios
   - id_projeto_usuarios|id_usuario


### Atividades

 - tabela_atividade
   - id_atividade|nome_adividade|id_projeto|id_notificacao

 - tabela_atividade_cronograma
   - id_crono_atividade|id_atividade|data_inicial|data_limite|data_fechamento|id_status

 - tabela_atividade_usuarios
   - id_atividade_usuarios|id_usuario


### Tarefas

 - tabela_tarefa
   - id_tarefa|descr_tarefa|id_projeto|id_notificacao

 - tabela_tarefa_cronograma
   - id_crono_tarefa|id_tarefa|data_inicial|data_limite|data_fechamento|id_status

 - tabela_tarefa_usuarios
   - id_tarefa_usuarios|id_usuario


 - tabela_tarefa_horas
   - id_tarefa_horas|id_tarefa|id_usuario|observacao




### Controles

 - tabela_status
   - id_status|descr_status
     - 1|Aberto
     - 2|Fechado


- tabela_notificacao
  - id_notificacao|descr_notificacao|cor_hex
    - 1|em Andamento|verde
    - 2|Atrasado|vermelho
    - 3|com Pendências|amarelo
    - ~~4|Fechado|cinza~~


 - tabela_controle
   - id_controle|descr_controle
     - 1|Criar
     - 2|Modificar
     - 3|Deletar
     

### Logs

 - tabela_log_usuario
   - id_log_usuario|id_user|timestamp|id_controle|descr_log


 - tabela_log_grupo
   - id_log_grupo|id_user|timestamp|id_controle|id_user_afetado|id_grupo|descr_log

 - tabela_log_cargo
   - id_log_cargo|id_user|timestamp|id_controle|id_cargo|descr_log


 - tabela_log_equipe
   - id_log_equipe|id_user|timestamp|id_controle|id_equipe|descr_log

- tabela_log_time
   - id_log_equipe|id_user|timestamp|id_controle|id_time|descr_log



 - tabela_log_cliente
   - id_log_cliente|timestamp|id_controle|id_user|id_cliente|descr_log

- tabela_log_projeto
   - id_log_projeto|timestamp|id_controle|id_user|id_cliente|id_projeto|descr_log

- tabela_log_atividade
   - id_log_atividade|timestamp|id_controle|id_user|id_cliente|id_projeto|id_atividade|descr_log

- tabela_log_tarefa
   - id_log_tarefa|timestamp|id_controle|id_user|id_cliente|id_projeto|id_atividade|id_tarefa|descr_log



## Modulos e rotas

 ### Modulo

- Clientes
    - Projeto
      - Atividade
        - Tarefa


- Usuarios


- Equipe


- Time

### Rotas

 - Rotas:
   - Adicionar
   - Modificar
   - Deletar


 - http://url/MODULO/ROTA
   - ex: http://url/Clientes/Adicionar

 
## Telas
 
 - Tela de login
   - url/login
   - url/logout
   

 - Tela Home
   - url/home



 - Cadastro de Usuários/Equipes/Times
   - url/usuario/{id_usuario}
   - url/equipe/{id_equipe}
   - url/time/{id_time}


 - Cadastro de Clientes/Projetos/Atividades/Tarefas
   -  url/cliente/{id_cliente}
   -  url/projeto/{id_projeto}
   -  url/atividade/{id_atividade}
   -  url/tarefa/{id_tarefa}
 


# Desenvolvimento

## Ambiente

 - para backend será usado Python3 e Flask:
   - configurar porta em arquivo credentials/config/ini ??? 
     - ou usar default do flask ??? -> passar por parametro ???


 - para BD será usado Postgres
   -  adicionar dados do BD em arquivo credentials/config/ini
     - url_bd
     - port_bd
     - nome_bd
     - user_bd
     - passwd_bd
 

 - oferecer versão em docker ???
   - se der tempo, colocar flask e postgres no docker 


