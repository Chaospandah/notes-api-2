# Debug Log #2 – ["422 Unprocessable Content"]

**Date:** 2025-11-26  
**Project:** Notes API  
**File(s):** main.py  

---

## 1. Symptom

- What I saw:
  - I saw a 422 Error: Unprocessable Content

## 2. Context

- What I did:
  - `added a new note_id`
- Result:
  - `422 Error`

## 3. Investigation

- Checked the data I was trying to add.
- Noticed the data was in the wrong format.

## 4. Root Cause

- Typo in the data entry: I put 999 instead of "999", so it was interpreted as an int and not a str so it returned 422 error.

## 5. Fix

- Updated the data type:

```python
# Before
{
  "title": 999,
  "content": 123
}

# After
{
  "title": "999",
  "content": "123"
}