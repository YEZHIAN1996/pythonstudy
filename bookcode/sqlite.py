import sqlite3
import os
import json

dbPath = 'data.sqlite'

if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''create table persons
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary real);''')
    conn.commit()
    conn.close()
    print('创建数据库成功')

conn = sqlite3.connect(dbPath)
c = conn.cursor()
c.execute('delete from persons')
print('删除成功')

c.execute('insert into persons(id,name,age,address,salary) values(1,"Paul",32,"beijing",2000.00)')
c.execute('insert into persons(id,name,age,address,salary) values(2,"tom",34,"shanghai",4000.00)')
c.execute('insert into persons(id,name,age,address,salary) values(3,"tim",12,"hangzhou",2300.00)')
c.execute('insert into persons(id,name,age,address,salary) values(4,"kate",22,"guangzhou",11000.00)')

conn.commit()
print('插入成功')

persons = c.execute('select name,age,address,salary from persons order by id')
print(type(persons))
result = []
for person in persons:
    value = {}
    value['name'] = person[0]
    value['age'] = person[1]
    value['address'] = person[2]
    result.append(value)

conn.close()
print(result)

resultStr = json.dumps(result)
print(type(resultStr))
print(resultStr)