from mysql_db import pool

class UserDao:
    # 登陆验证
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(*) from t_user where username=%s and AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 用户角色查询
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select r.role from t_user u join t_role r on u.role_id=r.id where u.username=%s'
            cursor.execute(sql, [username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()



