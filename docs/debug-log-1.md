# Debug Log #1 – [Short Title, e.g. "Broken /notes Route"]

**Date:** 2025-11-25  
**Project:** Notes API  
**File(s):** main.py  

---

## 1. Symptom

- What I saw:
  - Example: Hitting `GET /notes/1` returned `{"detail": "Not Found"}` instead of the note.

## 2. Context

- Command I ran:
  - `uvicorn main:app --reload`
- Endpoint:
  - `GET http://127.0.0.1:8000/notes/1`

## 3. Investigation

- Checked the FastAPI route decorator in `main.py`.
- Noticed the path was `"/notez/{note_id}"` instead of `"/notes/{note_id}"`.
- Confirmed in the `/docs` UI that there was no `GET /notes/{note_id}` route, only `GET /notez/{note_id}`.

## 4. Root Cause

- Typo in the route path: I registered `"/notez/{note_id}"` instead of `"/notes/{note_id}"`, so requests to `/notes/{note_id}` did not match any route and returned 404.

## 5. Fix

- Updated the decorator:

```python
# Before
@app.get("/notez/{note_id}")

# After
@app.get("/notes/{note_id}")
