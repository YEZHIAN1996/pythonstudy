from db.mysql_db import pool

class NewsDao:
    # 查询未审批列表
    def search_unreview_list(self,page):
        try:
            con = pool.get_connection()
            cursor=con.cursor()
            sql="select * " \
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
            cursor=con.cursor()
            sql="select ceil(count(*)/10) from t_news where state=%s"
            cursor.execute(sql, ["未审批"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

