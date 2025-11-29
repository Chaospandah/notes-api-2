import requests

BASE = "https://notes-api-2-cwol.onrender.com/"

# GET test
print("GET /notes")
print(requests.get(f"{BASE}/notes").json())

# POST test (valid)
print("\nPOST /notes (valid)")
print(requests.post(f"{BASE}/notes", json={
    "title": "Python Test",
    "content": "Testing with requests lib"
}).json())

# POST test (invalid)
print("\nPOST /notes (invalid)")
resp = requests.post(f"{BASE}/notes", json={
    "title": 123,
    "content": ["wrong"]
})
print(resp.status_code, resp.text)
