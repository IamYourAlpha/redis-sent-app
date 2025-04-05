import redis
import time

cache = redis.Redis(host='redis', port=6379, charset="utf-8", decode_response=True)

def addToCache(c1, c2, score):
    payload = {
        "c1": c1,
        "c2": c2,
        "score": score
    }
    key = "timestamp_" + str(time.time())
    cache.hset(key, mapping=payload)

def retrieve():
    queryList = []
    keys = cache.keys("timestamp_*")
    for key in keys:
        query = cache.hgetall(key)
        queryList.append(query)
    return queryList
