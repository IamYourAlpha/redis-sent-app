from fastapi import FastAPI
import redis

conn = redis.Redis(host='redis-database', port=6379,charset="utf-8",decode_responses=True)
conn.set("Intisar","Faiza") # Docker:Compose
ans = conn.get("Intisar")

app = FastAPI()

@app.get("/")
async def root():
    return "Docker: " + ans