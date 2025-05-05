[Português](README.md) | [English](README.en.md)

# 🐦 Mini-Twitter API

Uma aplicação backend que simula uma rede social de microblogs (estilo Twitter) com funcionalidades essenciais como criação de usuários, postagens, curtidas e sistema de seguidores.

## 📚 Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Execução (Docker)](#instalação-e-execução-docker)
- [Endpoints da API](#endpoints-da-api)
- [Autenticação](#autenticação)
- [Scripts Úteis](#scripts-úteis)
- [Possíveis Erros e Soluções](#possíveis-erros-e-soluções)
- [Contribuição](#contribuição)

---

## ⚙️ Tecnologias Utilizadas

- **Backend**: [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org/)
- **Banco de Dados**: [PostgreSQL](https://www.postgresql.org/)
- **Containerização**: [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/)

---

## 🗂️ Estrutura do Projeto

```
mini-twitter/
├── app
├── docker-compose.yml
├── Dockerfile
└── requeriments.txt
```


---

## 🐳 Instalação e Execução

> Pré-requisitos: git e python instalados.

```bash
# Clona o repositório em sua pasta local
git clone https://github.com/pedrohcdsouza/mini-twitter.git
# Acesse o repositório
cd mini-twitter
```

> Pré-requisitos: Docker e Docker Compose instalados.

```bash
# Suba a aplicação completa (backend e banco)
docker-compose up --build
```

## 📡 Endpoints da API

![endpoints](https://github.com/pedrohcdsouza/mini-twitter/blob/main/image.png)

## ❓ Como utilizar

Para testar os endpoints da API, utilize uma ferramenta de requisições HTTP — como o [Postman](https://www.postman.com/) (recomendado).

Siga os passos abaixo:

1. Abra o Postman (ou ferramenta similar).
2. Configure a URL do endpoint que deseja testar (localhost:8000).
3. Selecione o **método HTTP correto** (GET, POST, PUT, DELETE, etc.).
4. Adicione os parâmetros, cabeçalhos ou corpo da requisição, conforme necessário.
5. Envie a requisição e analise a resposta retornada pela API.

Lembre-se de seguir os exemplos descritos acima para cada endpoint.


