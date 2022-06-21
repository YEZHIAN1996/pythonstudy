from db.mysql_db import pool

class UserDao:
    # 验证登录
    def login(self, username, password):
        try:
            con = pool.get_connecton()
            cursor = con.cursor()
            sql = "select count(*) from user where username=%s and password=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
