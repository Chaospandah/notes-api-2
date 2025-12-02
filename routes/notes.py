from fastapi import APIRouter, HTTPException
from app.models.note import Note, NoteCreate, NoteUpdate

router = APIRouter()

# In-memory database
notes_db = [
    {"id": 1, "title": "First note", "content": "Hello  world"},
    {"id": 2, "title": "Second note", "content": "APIs are kinda fun ngl (im lying)"},
]



@router.get("/notes", response_model=list[Note])
def list_notes():
    return notes_db


@router.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@router.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate):
    new_id = max([n["id"] for n in notes_db]) + 1 if notes_db else 1

    new_note = {
        "id": new_id,
        "title": note.title,
        "content": note.content,
    }

    notes_db.append(new_note)
    return new_note


@router.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, updated_note: NoteUpdate):
    for note in notes_db:
        if note["id"] == note_id:
            if updated_note.title is not None:
                note["title"] = updated_note.title
            if updated_note.content is not None:
                note["content"] = updated_note.content
            return note

    raise HTTPException(status_code=404, detail="Note not found")


@router.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    for index, note in enumerate(notes_db):
        if note["id"] == note_id:
            notes_db.pop(index)
            return

    raise HTTPException(status_code=404, detail="Note not found")
