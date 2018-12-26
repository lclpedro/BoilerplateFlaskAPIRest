# INIT APP FLASK API REST
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


### Todos os passos foram seguidos da documentação, leia atentamente ela e siga em frente na construção do seu projeto.