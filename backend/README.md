## API
A API contém os seguintes endpoints:


### Cadastrar usuários
Cadastra usuários no sistema

#### Requisição
```
POST /register/
{
  "username": "renato",
  "email": "renato@renato.com",
  "password": "password"
}
```

#### Retorno
```json
{
  "username": "renato",
  "email": "renato@renato.com"
}
```


### Obter Token
Obtém Token, a partir dos dados do usuário

#### Requisição
```
POST /api-token-auth/
{
  "username": "renato",
  "password": "password
}
```

#### Retorno
```json
{
  "token": "78d69daf9a8759fe6c2b6d5a78ae2b041e7484f9"
}
```


### Autenticação
Com exceção dos endpoints de obtenção de Token e cadastro de usuários, todos os endpoints da API são protegidos por autenticação e necessitam receber token via cabeçalho HTTP `Authorization`. Veja um exemplo de requisição:

```
GET /especialidades/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```


### Listar especialidades médicas
Lista todas as especialidades médicas disponíveis na clínica

#### Requisição
```
GET /especialidades/
```

#### Resposta
```json
[
    {
      "id": 1,
      "nome": "Pediatria"
    },
    {
      "id": 2,
      "nome": "Ginecologia"
    },
    {
      "id": 3,
      "nome": "Cardiologia"
    },
    {
      "id": 4,
      "nome": "Clínico Geral"
    }
]
```

#### Filtros
* Nome da especialidade (termo de pesquisa)

```
GET /especialidades/?search=ped
```


### Listar médicos
Lista todos os médicos que atendem pela clínica

#### Requisição
```
GET /medicos/
```

#### Retorno
```json
[
    {
      "id": 1,
      "crm": 3711,
      "nome": "Drauzio Varella",
      "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
    },
    {
      "id": 2,
      "crm": 2544,
      "nome": "Gregory House",
      "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
    },
    {
      "id": 3,
      "crm": 3087,
      "nome": "Tony Tony Chopper",
      "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
    }
]
```

#### Filtros
* Identificador de uma ou mais especialidades
* Nome do médico (termo de pesquisa)

```
GET /medicos/?search=maria&especialidade=1&especialidade=3
```


### Listar consultas marcadas
Lista todas as consultas marcadas do usuário logado

#### Requisição
```
GET /consultas/
```

#### Retorno
```json
[
    {
      "id": 1,
      "dia": "2020-02-05",
      "horario": "12:00",
      "data_agendamento": "2020-02-01T10:45:0-03:00",
      "medico": {
        "id": 2,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
      }
    },
    {
      "id": 2,
      "dia": "2020-03-01",
      "horario": "09:00",
      "data_agendamento": "2020-02-01T10:45:0-03:00",
      "medico": {
        "id": 1,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
      }
    }
]
```


### Listar agendas disponíveis
Lista todas as agendas disponíveis na clínica

#### Requisição
```
GET /agendas/
```

#### Retorno
```json
[
    {
      "id": 1,
      "medico": {
        "id": 3,
        "crm": 3087,
        "nome": "Tony Tony Chopper",
        "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
      },
      "dia": "2020-02-10",
      "horarios": ["14:00", "14:15", "16:00"]
    },
    {
      "id": 2,
      "medico": {
        "id": 2,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
      },
      "dia": "2020-02-10",
      "horarios": ["08:00", "08:30", "09:00", "09:30", "14:00"]
    }
]
```

#### Filtros
* Identificador de um ou mais médicos
* Identificador de uma ou mais especialidades
* Intervalo de data

```
GET /agendas/?medico=1&especialidade=2&data_inicio=2020-01-01&data_final=2020-01-05
```


### Marcar consulta
Marca uma consulta para o usuário logado

#### Requisição
```
POST /consultas/
{
  "agenda_id": 1,
  "horario": "14:15"
}
```

#### Retorno

```json
{
  "id": 2,
  "dia": "2020-03-01",
  "horario": "09:00",
  "data_agendamento": "2020-02-01T10:45:0-03:00",
  "medico": {
    "id": 1,
    "crm": 3711,
    "nome": "Drauzio Varella",
    "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
  }
}
```


### Desmarcar consulta
Desmarca uma consulta marcada pelo usuário

#### Requisição
```
DELETE /consultas/<consulta_id>
```

#### Retorno
Não há retorno (vazio)