from redis_db import pool
import redis

r = redis.Redis(
    connection_pool=pool
)
try:
    r.lpush('dname', '董事会', '秘书处', '财务部', '技术部')
    r.lpop('dname')
    result = r.lrange('dname',0,-1)
    for one in result:
        print(one.decode('utf-8'))

    r.sadd('employee', 8001, 8002, 8003)
    r.srem('employee', 8002)
    result = r.smembers('employee')
    for one in result:
        print(one.decode('utf-8'))

    r.zadd('keyword', {'马云':0,'张朝阳':0,'丁磊':0})
    r.zincrby("keyword", 10, '马云')
    result = r.zrevrange('keyword', 0, -1)
    for one in result:
        print(one.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del r