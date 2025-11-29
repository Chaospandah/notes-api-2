# Debug Log #3 – ["Deployment Failure on Render"]

**Date:** 2025-11-28  
**Project:** Notes API  
**System:** Render Web Service  

---

## 1. Symptom

- What I saw:
  - Deployment failed during the Build phase.

## 2. Context

- What I did:
  - Pushed code to Github
  - Triggered auto-deploy on Render
- Result:
  - `Deployment Error`

## 3. Investigation

- Checked requirements.txt → missing FastAPI
- Verified main.py exists in repo root

## 4. Root Cause

- Missing uvicorn in requirements.txt

## 5. Fix

- Added missing dependency
- Re-deployed

## 6 Prevention

- Always regenerate requirements.txt after installing packages