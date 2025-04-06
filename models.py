import json
import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse



API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
tokenPath = "./keys/token.txt"

# Read the token (my personal token)
with open(tokenPath, "r") as f:
    tok = f.read().strip() 

headers = {"Authorization": f"Bearer {tok}"}  # add "Bearer " prefix

# todo:
# replace followint with on-device model.
app = FastAPI()
@app.post("/predict", response_class=JSONResponse)
async def predict(request: Request):
    data = await request.json()
    str1 = data.get("str1")
    str2 = data.get("str2")
    payload = {
        "inputs": {
            "source_sentence": str1,
            "sentences": [str2] # can be a list.
        }
    }
    # in header I have the token info, and payload contains the sentence I want to process.
    response = requests.post(API_URL, headers=headers, json=payload)
    print (response)
    if response.status_code == 200:
        return JSONResponse(content=response.json())
    else:
        error = {"error": response.status_code, "message": response.text}  # Handle errors
        return JSONResponse(content=error)
    
# if __name__ == "__main__":
#     str1 = "I like orange"
#     str2 = "I do not like orange"
#     response = requests.post("http://localhost:8000/predict", json={"str1": "hello", "str2:": "world"})
#     result = predict(str1, str2)
#     print(json.dumps(result, indent=2))
