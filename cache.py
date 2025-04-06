import redis
import time

cache = redis.Redis(host='redis-database', port=6379, charset="utf-8", decode_responses=True)

def addToCache(c1, c2, score):
    payload = {
        "c1": c1,
        "c2": c2,
        "score": score
    }
    key = "timestamp_" + str(time.time())
    cache.hset(key, mapping=payload)

def cleanCache():
    keys = cache.keys("*")
    # x == ['prefix:key1','prefix:key2'] # True
    for key in keys:
        cache.delete(key)

def retrieve():
    queryList = []
    keys = cache.keys("timestamp_*")
    for key in keys:
        query = cache.hgetall(key)
        queryList.append(query)
        # keyList.append(key)
    return queryList
# addToCache("intisar", "chowdhury", 10)
