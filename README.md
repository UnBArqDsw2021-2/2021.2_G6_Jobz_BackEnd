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

    make build

### Subir o ambiente:
    make run

### Parar o ambiente:
    make stop

### Comandos extras:
Entrar no container do banco de dados
    
    make db

Entrar no container do backend
    
    make backend

Fazer migração de modelo
     
     make migrate


