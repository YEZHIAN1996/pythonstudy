from mysql.connector.pooling import MySQLConnectionPool

__config = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "yza0404..",
    "database": "news"
}

try:
    pool = MySQLConnectionPool(**__config, pool_size=10)
except Exception as e:
    print(e)
