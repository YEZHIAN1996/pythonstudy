from pymysql import *
import json

def connectDB():
    db = connect("localhost", "root", "123456", "test", charset='utf-8')
    return db

db = connectDB()

def createTable(db):
    cursor = db.cursor()
    sql = '''create table persons
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary real);'''

    try:
        cursor.excute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    return False

def insertRecords(db):
    cursor = db.cursor()
    try:
        cursor.excute('delete from persons')
        cursor.execute('insert into persons(id,name,age,address,salary) values(1,"Paul",32,"beijing",2000.00)')
        cursor.execute('insert into persons(id,name,age,address,salary) values(2,"tom",34,"shanghai",4000.00)')
        cursor.execute('insert into persons(id,name,age,address,salary) values(3,"tim",12,"hangzhou",2300.00)')
        cursor.execute('insert into persons(id,name,age,address,salary) values(4,"kate",22,"guangzhou",11000.00)')
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
    return False

def selectRecords(db):
    cursor = db.cursor()
    sql = 'select name,age,salary from persons order by age desc'
    cursor.excute(sql)
    results = cursor.fetchall()
    print(results)
    fields = ['name', 'age', 'salary']
    recordes = []
    for row in results:
        recordes.append(dict(zip(fields, row)))
    return json.dumps(recordes)

if createTable(db):
    print('成功创建persons表')
else:
    print('persons表已经存在')

if insertRecords(db):
    print('成功插入记录')
else:
    print('插入记录失败')

print(selectRecords(db))
db.close()
