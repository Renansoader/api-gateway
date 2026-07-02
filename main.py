from fastapi import FastAPI
import httpx

app = FastAPI()

TASK_SERVICE_URL = "http://127.0.0.1:8000"

@app.post("/gateway/tasks")
async def criar_tarefa(nome: str):
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{TASK_SERVICE_URL}/tasks", params={"nome": nome})
        return r.json()

@app.get("/gateway/tasks/{job_id}")
async def status_tarefa(job_id: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{TASK_SERVICE_URL}/tasks/{job_id}")
        return r.json()