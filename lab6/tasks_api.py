from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="REST API — Список задач")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Изучить Python", "completed": True},
    {"id": 2, "title": "Изучить FastAPI", "completed": False}
]


@app.get("/")
def home():
    return {"message": "REST API для списка задач"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def add_task(task: Task):
    new_task = {
        "id": max([item["id"] for item in tasks], default=0) + 1,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")
