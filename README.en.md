[Portuguese](README.md) | [English](README.en.md)

# 🐦 Mini-Twitter API

A backend application that simulates a microblogging social network (similar to Twitter), with essential features such as user creation, posting, likes, and a follower system.

## 📚 Table of Contents

- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation and Execution (Docker)](#installation-and-execution-docker)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Useful Scripts](#useful-scripts)
- [Possible Errors and Solutions](#possible-errors-and-solutions)
- [Contribution](#contribution)

---

## ⚙️ Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **Containerization**: [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/)

---

## 🗂️ Project Structure

```
mini-twitter/
├── app
├── docker-compose.yml
├── Dockerfile
└── requeriments.txt
```

---

## 🐳 Installation and Execution

> Prerequisites: Git and Python installed.

```bash
# Clone the repository to your local folder
git clone https://github.com/pedrohcdsouza/mini-twitter.git
# Navigate into the repository
cd mini-twitter
```

> Prerequisites: Docker and Docker Compose installed.

```bash
Prerequisites: Docker and Docker Compose installed.
```

📡 API Endpoints

![endpoints](https://github.com/pedrohcdsouza/mini-twitter/blob/main/image.png)

❓ How to Use

To test the API endpoints, use an HTTP request tool — such as Postman (recommended).

Follow the steps below:

    Open Postman (or any similar tool).

    Set the endpoint URL you want to test (e.g., localhost:8000).

    Select the correct HTTP method (GET, POST, PUT, DELETE, etc.).

    Add parameters, headers, or request body as needed.

    Send the request and analyze the response returned by the API.

Make sure to follow the examples provided above for each endpoint.

