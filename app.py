from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="API Integration Demo")
EXTERNAL_API_URL = "https://jsonplaceholder.typicode.com"

# Task 2 & 4: Make GET request and Integrate
@app.get("/fetch-data/{item_id}")
def fetch_data(item_id: int):
    response = requests.get(f"{EXTERNAL_API_URL}/posts/{item_id}")
    
    # Task 5: Handle errors and unsuccessful responses
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from external API")
    
    # Task 3: Parse JSON response
    parsed_json = response.json()
    return {"message": "Data retrieved successfully", "data": parsed_json}

# Task 2 & 4: Make POST request and Integrate
@app.post("/submit-data")
def submit_data(title: str, body: str, user_id: int = 1):
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{EXTERNAL_API_URL}/posts", json=payload)
    
    # Task 5: Handle errors
    if response.status_code not in (200, 201):
        raise HTTPException(status_code=response.status_code, detail="Failed to push data to external API")
        
    # Task 3: Parse JSON response
    return {"message": "Data posted successfully", "data": response.json()}