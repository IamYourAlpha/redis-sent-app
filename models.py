import json
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
tokenPath = "./token.txt"

# Read the token (my person token)
with open(tokenPath, "r") as f:
    tok = f.read().strip() 

headers = {"Authorization": f"Bearer {tok}"}  # Add "Bearer " prefix

# todo:
# replace followint with on-device model.
def predict(str1, str2):
    payload = {
        "inputs": {
            "source_sentence": str1,
            "sentences": [str2] # can be a list.
        }
    }
    # in header I have the token info, and payload contains the sentence I want to process.
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}  # Handle errors

if __name__ == "__main__":
    str1 = "I like orange"
    str2 = "I do not like orange"
    
    result = predict(str1, str2)
    print(json.dumps(result, indent=2))
