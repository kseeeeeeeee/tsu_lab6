from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="REST API — Заметки")


class Note(BaseModel):
    title: str
    content: str


notes = [
    {"id": 1, "title": "Первая заметка", "content": "Изучить основы FastAPI"},
    {"id": 2, "title": "Планы", "content": "Выполнить лабораторную работу"}
]


@app.get("/")
def home():
    return {"message": "REST API для заметок"}


@app.get("/notes")
def get_notes():
    return notes


@app.post("/notes")
def create_note(note: Note):
    new_note = {
        "id": max([item["id"] for item in notes], default=0) + 1,
        "title": note.title,
        "content": note.content
    }
    notes.append(new_note)
    return new_note


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Заметка не найдена")


@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = updated_note.title
            note["content"] = updated_note.content
            return note
    raise HTTPException(status_code=404, detail="Заметка не найдена")


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Заметка удалена"}
    raise HTTPException(status_code=404, detail="Заметка не найдена")
