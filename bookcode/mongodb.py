from pymongo import *

Client = MongoClient()
db = Client.data  # 或者 db = Client['data']
