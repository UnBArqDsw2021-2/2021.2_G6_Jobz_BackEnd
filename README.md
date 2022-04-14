# Jobz

**Código da Disciplina**: FGA0208<br>
**Número do Grupo**: 06<br>

## Alunos

| Matrícula  | Aluno                            | GitHub                                                 |
| ---------- | -------------------------------- | ------------------------------------------------------ |
| 18/0012002 | Álvaro Gouvea                    | [@AlGouvea](https://github.com/AlGouvea)               |
| 20/2028211 | Antonio Aldisio                  | [@AntonioAldisio](https://github.com/AntonioAldisio)   |
| 17/0006328 | Ariel Vieira Lima Serafim        | [@ArielSixwings](https://github.com/ArielSixwings)     |
| 19/0106565 | Fernando Miranda Calil           | [@ilus1](https://github.com/ilus1)                     |
| 18/0018159 | Guilherme Braz                   | [@GuilhermeBraz](https://github.com/GuilhermeBraz)     |
| 17/0013987 | João Victor de Oliveira Matos    | [@joao15victor08](https://github.com/joao15victor08)   |
| 19/0032863 | Lorrayne Alves Cardozo           | [@LorrayneCardozo](https://github.com/LorrayneCardozo) |
| 18/0042661 | Luis Fernando Furtado De Araújo  | [@luis-furtado](https://github.com/luis-furtado)       |
| 19/0036435 | Pedro Henrique Carvalho Campos   | [@Peh099](https://github.com/Peh099)                   |
| 19/0048221 | Rodrigo Balbino Azevedo de Brito | [@Balbinoo](https://github.com/Balbinoo)               |


## Requisitos

Docker => 20.10.12

docker compose => 1.29.2

## Como rodar
### Primeira execução:

- Primeiro você deve criar as imagens necessárias para rodar o ambiente, para isso você deve usar o comando:

```
    make build
```

- Em seguida é necessário subir os containers do ambiente com o comando:
```
    make run
```

- Por fim é necessário executar as migrations com o comando:
```
    make migrate
```

### Possiveis erros
```
    tcp4 0.0.0.0:5432: bind: address already in use
```

- Solução
```
    sudo ss -lptn 'sport = :5432'
```
Que deve retornar uma mensagem parecida com:
```
State   Recv-Q  Send-Q     Local Address:Port          Peer Address:Port       Process
LISTEN  0       244            127.0.0.1:5432               0.0.0.0:*           users:(("postgres",pid=1006,fd=3))
```
em seguida você deve matar o processo com:
```
sudo kill -9 1006(o pid que é retornado na mensagem acima)
```
```
sudo fuser -k 5432/tcp
```

### Comandos individuais:

- Subir containers de ambiente:
```
    make run
```

- Parar containers de ambiente:
```
    make stop
```

- Entrar no container do banco de dados
```
    make db
```
- Acesso ao posgres (você deve estar dentro do container do banco):
```
    psql -U postgres -W
```
    Senha do banco: postgres


- Entrar no container do backend:
```
    make backend
```

- Fazer migração de alterações em tabelas do django para que elas reflitam nas tabelas do banco de dados:
```
     make migrate
```

### Endpoints

- User

    localhost:8000/user/

    - Atributos

        "cpf": (integer)<br>
        "name": (string)<br>
        "phone": (integer)<br>
        "email": (string)<br>
        "password": (string)

- Provider

    localhost:8000/provider/

    - Atributos

        "cpf": (integer)<br>
        "name": (string)<br>
        "phone": (integer)<br>
        "email": (string)<br>
        "occupation": (int) <-- ID da occupation<br>
        "password": (string)

- Schedule(precisa estar logado)

    localhost:8000/schedule/

    - Atributos

        "dayOfWeek": ("seg", "ter", "qua", "qui", "sex", "sab", "dom")<br>
        "entryTime": ("HH:MM:SS")<br>
        "endOfWork": ("HH:MM:SS")<br>
        "provider": cpf(do provider)

- Service(precisa estar logado)

    localhost:8000/service/

    - Atributos

        "dateService": YYYY-MM-DD  <-- Tudo integer<br>
        "serviceDescription": (string)<br>
        "user": cpf(do usuário)<br>
        "provider": cpf(do provider)<br>
        "occupation": idOccupation <-- Precisa cadastrar uma occupation

- Occupation(precisa estar logado)

    Não deveria ser acessivel pelo site normal<br>
    Não pode ter categorias com mesmo nome<br>
    Só tem algumas possibilidades (as que tem no modelo do FrontEnd)

    - Atributos

        "occupation": enum(Encanador, Diarista, Pedreiro,Tecnico)

- Login

    localhost:8000/api/token/obtain/

    - Atributos

        "email": (string)
        "password": (string)

    **Retorna dois tokens que precisam ser passados como authorization header(JWT ou Bearer) para as paginas que precisam de autenticação.**

- Pesquisa

    localhost:8000/provider/**Provider**/**Occupation**

    - **Provider** = Uma string com parte do nome do prestador de serviço cadastrado, deve serguir o mesmo padrão do cadastro (deve ser case sensitive, etc), ou um "-" caso não deseje fazer pesquisa especificando nome do prestador.
    - **Occupation** = Um int, que corresponde ao ID da categoria que irá fazer parte do filtro, deve passar o numero "0" quando não quiser especificar uma ocupação.
    


- Perfil
    localhost:8000/provider/**CPF**/

    - **CPF** = CPF cadastrado do usuário.

    - Atributos:
        "cpf": (integer)<br>
        "name": (string)<br>
        "phone": (integer)<br>
        "email": (string)<br>
        "occupation": (int) <-- ID da occupation<br>
        "password": (string)<br>
        "photo": imagem ou null


    **Todos os campos podem ser alterados pelo mesmo body que está no formulário de cadastro, também tem as mesmas restrições, inclusive a parte de inserir a senha, que pode ser a mesma ou uma nova senha(vamos mudar isso em breve).**
