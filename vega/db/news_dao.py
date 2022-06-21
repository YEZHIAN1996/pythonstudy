from db.mysql_db import pool

class NewsDao:
    # 查询未审批新闻列表
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                "join t_user u on n.editor_id=u.id " \
                "where n.state=%s " \
                "and order by n.create_time desc " \
                "limit %s,%s"
            cursor.execute(sql, ("未审批", (page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询未审批新闻的总页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_news where state=%s"
            cursor.execute(sql, ["未审批"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 更新待审批的新闻为审批状态
    def update_unreview_news(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "update t_news set state=%s where id=%s"
            cursor.execute(sql, ("已审批", id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询所有新闻
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                "join t_user u on n.editor_id=u.id " \
                "order by n.create_time desc " \
                "limit %s,%s"
            cursor.execute(sql, ((page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询新闻总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 根据id删除某条新闻
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "delete from t_news where id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
