from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    file = open('a.txt', mode='r', encoding='utf-8')
    data = file.read().splitlines()
    for one in data:
        temp = one.split(',')
        sid = temp[0]
        name= temp[1]
        classno = temp[2]
        score_1 = int(temp[3])
        score_2 = int(temp[4])
        score_3 = int(temp[5])
        if score_1>85 and score_2>85 and score_3>85:
            con.hmset(sid,{'name':name,'classno':classno,'score_1':score_1,
                           'score_2':score_2,'score_3':score_3})
    print('执行成功')
except Exception as e:
    print(e)
finally:
    if 'file' in dir():
        file.close()
    del con