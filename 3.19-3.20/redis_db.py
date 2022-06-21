import redis

try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        password="abc123456",
        db=0,
        max_connections=20
    )
except Exception as e:
    print(e)