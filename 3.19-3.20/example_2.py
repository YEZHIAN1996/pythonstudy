from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    # con.hmset('9527', {'name':'yezhian','age':26,'sex':'男'})
    con.hset('9527','city','fuzhou', {'name':'yezhian','age':26,'sex':'男'})
    # con.delete('9527','age')
    result1 = con.hexists('9527', 'name')
    print(result1)
    result2 = con.hgetall('9527')
    for one in result2:
        print(one.decode('utf-8'), result2[one].decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con