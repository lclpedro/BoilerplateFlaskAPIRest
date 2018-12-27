# INIT APP FLASK API REST
A intenção do INIT APP FLASK API REST é criar um boilerplate consistente para ser aplicado nos projetos de desenvolvimento de APIs, os mesmos modelos estão sendo desenvolvidos e aplicados seguinda regras descritas na documentação do próprio Flask.

Contribuia, e ajude a comunidade Flask crescer ainda mais.

### Instalando a lib virtualenv para separar a camada da aplicação da camada do python do S.O.
`$ sudo pip3 install virtualenv`

### Criando um novo container para aplicação chamada env com python3 
`$ virtualenv -p python3 env`

### Ativado a camada que acabou de ser criada
`source env/bin/activate`

### Instalando as dependências do projeto exitentes dentro do requirements.txt
`(env) $ pip install -r requirements.txt` 

### Já existindo todas as variáveis de ambiente cadastradas dentro do arquivo .env é só executar e começar a desenvolver.

`(env) $ flask run`

### Executando a aplicação em modo de produção no servidor.

Depois de ter seguido todos os passos e ter desenvolvido os seus módulos, chegou a hora de colocar a aplicação em modo de produção.
É bem simples, como a aplicação já foi configurada de uma forma simples pra executar os servidores basta executar o seguinte comando.

`(env) $ gunicorn run:create_app`



### Todos os passos foram seguidos da documentação, leia atentamente ela e siga em frente na construção do seu projeto.




Documentação Flask: http://flask.pocoo.org/docs/1.0/
Pallets Flask: https://palletsprojects.com/p/flask/
