from db.news_dao import NewsDao

class NewsService:
    __news_dao = NewsDao()

    # 查询未审批新闻列表
    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 查询未审批新闻的总页数
    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    # 更新待审批的新闻为审批状态
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # 查询所有新闻
    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

    # 查询新闻总页数
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    # 根据id删除某条新闻
    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)