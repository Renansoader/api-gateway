# API Gateway from Scratch

Gateway que centraliza requisições e as repassa para outros serviços — nesse caso, a API do projeto [Distributed Task Queue](https://github.com/Renansoader/distributed-task-queue).

## Stack

- **FastAPI** — API REST
- **httpx** — cliente HTTP assíncrono, usado para repassar requisições

## Como funciona

Um API Gateway é a porta de entrada única de um sistema. Em vez do cliente falar direto com cada serviço, ele fala com o gateway, que decide para onde encaminhar a requisição.

Aqui, o gateway recebe chamadas em `/gateway/...` e repassa para a API do Task Queue rodando na porta 8000.

## Endpoints

| Método | Rota | Repassa para |
|--------|------|---------------|
| POST | `/gateway/tasks` | `POST /tasks` (Task Queue) |
| GET | `/gateway/tasks/{job_id}` | `GET /tasks/{job_id}` (Task Queue) |

## Rodando localmente

Pré-requisito: o projeto `distributed-task-queue` rodando na porta 8000 (API + worker).

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn httpx python-dotenv
uvicorn main:app --reload --port 8001
```

Documentação interativa em `http://127.0.0.1:8001/docs`.

## Aprendizados

Projeto construído para praticar o padrão de arquitetura de gateway — desacoplamento de serviços, roteamento de requisições e comunicação entre APIs.
