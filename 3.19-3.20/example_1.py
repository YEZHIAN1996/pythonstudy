import redis
from redis_db import pool
import time

try:
    con = redis.Redis(
        connection_pool=pool
    )
    con.set("county", "英国")
    con.set("city", "伦敦")
    con.set('town', '花城')
    city = con.get("city").decode("utf-8")
    print(city)
    con.expire('town', 5)
    time.sleep(5)
    con.delete('county', 'city')
    con.mset({'city': 'shanghai','county':'china'})
    r = con.mget('city', 'county')
    for one in r:
        print(one.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con
