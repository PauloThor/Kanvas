<h1>Kanvas 🐶</h1>
O Kanvas é um sistema voltado para o ensino. É possível cadastrar estudantes, facilitadores e instrutores; além de uma extensa interação com cursos e atividades com permissões diferenciadas para cada tipo de usuário.

Ao utilizar esta API, deve ser possível criar informações de cursos e atividades, bem como listar ou excluir tais informações.

<h1>Como instalar e rodar? 🚀</h1>
Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

# Este passo é para baixar o projeto

git clone https://gitlab.com/paulothor/kanvas.git
Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

# Entrar na pasta

cd kanvast

# Criar um ambiente virtual

python3 -m venv venv

# Entrar no ambiente virtual

source venv/bin/activate
Então, para instalar as dependências, basta:

pip install -r requirements.txt
Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

./manage.py migrate
Então, para rodar, basta digitar o seguinte, no terminal:

./manage.py runserver
E o sistema estará rodando em http://127.0.0.1:8000/

Utilização 🖥️
Para utilizar este sistema, é necessário utilizar um API Client, como o Insomnia

Rotas

<h3>POST /api/accounts/</h3>
Esta rota cadastra um usuário.

RESPONSE STATUS -> HTTP 201 (created)
Body:

```json
{
  "username": "student",
  "password": "1234",
  "is_superuser": false,
  "is_staff": false
}
```

Response:

```json
{
  "id": 1,
  "username": "student",
  "is_superuser": false,
  "is_staff": false
}
```

<h3>POST /api/login/</h3>
Esta rota faz o login de um usuário.

RESPONSE STATUS -> HTTP 200 (ok)
Body:

```json
{
  "username": "student",
  "password": "1234"
}
```

Response:

```json
{
  "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

<h3>GET /api/courses/< int:course_id >/</h3>
Esta rota retorna as informações do curso com id igual ao passado na rota.

RESPONSE STATUS -> HTTP 200 (ok)

```json
[
  {
    "id": 1,
    "name": "Node",
    "users": [
      {
        "id": 3,
        "username": "student1"
      }
    ]
  },
  {
    "id": 2,
    "name": "Django",
    "users": []
  },
  {
    "id": 3,
    "name": "React",
    "users": []
  }
]
```

<h3>POST /api/courses/</h3>
Esta rota é para a criação de informações de animais.

RESPONSE STATUS -> HTTP 201 (created)
Body:

```json
{
  "name": "Node"
}
```

Response:

```json
{
  "id": 1,
  "name": "Node",
  "users": []
}
```

<h3>PUT /api/courses/< int:course_id ></h3>
Esta rota é para atualizar as informações de um curso.

RESPONSE STATUS -> HTTP 200 (ok)
Body:

```json
{
  "name": "Node"
}
```

Response:

```json
{
  "id": 1,
  "name": "Node",
  "users": []
}
```

<h3>PUT /api/courses/< int:course_id >/registrations/</h3>
Esta rota é para matricular os estudantes em um curso.

RESPONSE STATUS -> HTTP 200 (ok)
Body:

```json
{
  "user_ids": [3, 4, 5]
}
```

Response:

```json
{
  "id": 1,
  "name": "Node",
  "users": [
    {
      "id": 3,
      "username": "student1"
    },
    {
      "id": 4,
      "username": "student2"
    },
    {
      "id": 5,
      "username": "student3"
    }
  ]
}
```

<h3>GET /api/courses/</h3>
Esta rota retorna as informações de todos os cursos.

RESPONSE STATUS -> HTTP 200 (ok)

```json
[
  {
    "id": 1,
    "name": "Node",
    "users": [
      {
        "id": 3,
        "username": "student1"
      }
    ]
  },
  {
    "id": 2,
    "name": "Django",
    "users": []
  },
  {
    "id": 3,
    "name": "React",
    "users": []
  }
]
```

<h3>DELETE /api/courses/< int:course_id >/</h3>
Rota para deletar as informações de um curso.

Não há conteúdo no retorno da requisição.

RESPONSE STATUS -> HTTP 204 (no content)

<h3>POST /api/activities/</h3>
Esta rota é para cadastrar uma atividade.

RESPONSE STATUS -> HTTP 201 (ok)
Body:

```json
{
  "title": "Kenzie Pet",
  "points": 10
}
```

Response:

```json
{
  "id": 1,
  "title": "Kenzie Pet",
  "points": 10,
  "submissions": []
}
```

<h3>GET /api/activities/</h3>
Esta rota retorna as informações de todos os atividades.

RESPONSE STATUS -> HTTP 200 (ok)

```json
[
  {
    "id": 1,
    "title": "Kenzie Pet",
    "points": 10,
    "submissions": [
      {
        "id": 1,
        "grade": 10,
        "repo": "http://gitlab.com/kenzie_pet",
        "user_id": 3,
        "activity_id": 1
      }
    ]
  },
  {
    "id": 2,
    "title": "Kanvas",
    "points": 10,
    "submissions": [
      {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
      }
    ]
  }
]
```

<h3>PUT /api/activities/< int:activity_id >/</h3>
Esta rota é para atualizar as informações de uma atividade.

RESPONSE STATUS -> HTTP 200 (ok)
Body:

```json
{
  "title": "Kenzie Pet",
  "points": 10
}
```

Response:

```json
{
  "id": 1,
  "title": "Kenzie Pet",
  "points": 10,
  "submissions": []
}
```

<h3>PUT /api/activities/< int:activity_id >/submissions/</h3>
Esta rota é para um estudante fazer submissão de uma atividade.

RESPONSE STATUS -> HTTP 201 (created)
Body:

```json
{
  "grade": 10, // Esse campo é opcional
  "repo": "http://gitlab.com/kenzie_pet"
}
```

Response:

```json
{
  "id": 7,
  "grade": null,
  "repo": "http://gitlab.com/kenzie_pet",
  "user_id": 3,
  "activity_id": 1
}
```

<h3>PUT /api/activities/< int:activity_id >/submissions/</h3>
Esta rota é para um facilitador ou instrutor editar a nota de uma submissão.

RESPONSE STATUS -> HTTP 200 (ok)
Body:

```json
{
  "grade": 10
}
```

Response:

```json
{
  "id": 3,
  "grade": 10,
  "repo": "http://gitlab.com/kenzie_pet",
  "user_id": 3,
  "activity_id": 1
}
```

<h3>GET /api/submissions/</h3>
Esta rota retorna as informações de todos as submissões do estudante, ou de todos os estudantes se a requisição estiver sendo feita por um facilitador/instrutor.

RESPONSE STATUS -> HTTP 200 (ok)

Se for o token de um estudante:

```json
[
  {
    "id": 2,
    "grade": 8,
    "repo": "http://gitlab.com/kanvas",
    "user_id": 4,
    "activity_id": 2
  },
  {
    "id": 5,
    "grade": null,
    "repo": "http://gitlab.com/kmdb2",
    "user_id": 4,
    "activity_id": 1
  }
]
```

Se for o token de um facilitador ou instrutor:

```json
[
  {
    "id": 1,
    "grade": 10,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
  },
  {
    "id": 2,
    "grade": 8,
    "repo": "http://gitlab.com/kanvas",
    "user_id": 4,
    "activity_id": 2
  },
  {
    "id": 3,
    "grade": 4,
    "repo": "http://gitlab.com/kmdb",
    "user_id": 5,
    "activity_id": 3
  },
  {
    "id": 4,
    "grade": null,
    "repo": "http://gitlab.com/kmdb2",
    "user_id": 5,
    "activity_id": 3
  }
]
```

<h1>Tecnologias utilizadas 📱</h1>
<ul>
<li>Django</li>
<li>Django Rest Framework</li>
<li>SQLite</li>
</ul>

<hr/>

<h1>Licence</h1>

MIT
