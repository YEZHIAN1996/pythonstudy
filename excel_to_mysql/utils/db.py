# coding:utf-8

import mysql.connector.pooling


class Mysql(object):
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'yza0404..',
            'database': 'stuinfo'
        }
        self.pool = self.get_pool()

    def get_pool(self):
        try:
            pool = mysql.connector.pooling.MySQLConnectionPool(**self.config, pool_size=10)
        except Exception as e:
            raise e
        return pool

    # 一键导入学生成绩信息
    def insert(self, table_name, stu_no, username, gender, Chinese_score, Math_score, English_score):
        try:
            con = self.pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO " + table_name + "(stu_no, username, gender, Chinese_score, Math_score, English_score) VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (stu_no, username, gender, Chinese_score, Math_score, English_score))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询学生成绩
    def search(self, table_name, name=''):
        try:
            con = self.pool.get_connection()
            cursor = con.cursor()
            if name == '':
                sql = "select * from " + table_name
                cursor.execute(sql)
            else:
                sql = "select * from " + table_name + "where username = %s"
                cursor.execute(sql, name)
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 清空表中所有学生成绩信息
    def delete_all(self, table_name):
        try:
            con = self.pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "truncate table " + table_name  # drop
            cursor.execute(sql,)
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 总成绩排名
    def total_score_sort(self, table_name):
        # TODO
        pass