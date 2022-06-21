from db.mysql_db import pool

class UserDao():
    # 验证用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(*) from t_user where username=%s " \
                  "and AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count==1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户的角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select r.role from t_user u join t_role on u.role_id = r.id " \
                  "where u.username=%S"
            cursor.execute(sql, [username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 插入用户
    def insert(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "insert into t_user(username, password, email, role_id) " \
                  "values(%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s) "
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_user"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户记录分页
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select u.id,u.username,r.role from t_user u join t_role r on u.role_id = r.id " \
                  "order by u.id limit %s,%s"
            cursor.execute(sql, ((page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改用户信息
    def update(self, id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "update t_user set username=%s,password=HEX(AES_ENCRYPT(%S, 'HelloWorld'))," \
                  "email=%s,role_id=%s where id=%s"
            cursor.execute(sql, (username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除用户信息
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "delete from t_user where id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()