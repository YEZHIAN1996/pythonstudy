from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # 插入用户
    def insert(self, username, password, email, role_id):
        self.__user_dao.insert(username, password, email, role_id)

    # 查询用户总页数
    def search_count_page(self):
        count_page = self.__user_dao.search_count_page()
        return count_page
    # 查询用户记录分页
    def search_list(self, page):
        result = self.__user_dao.search_list(page)
        return result

    # 修改用户信息
    def update(self, id, username, password, email, role_id):
        self.__user_dao.update( id, username, password, email, role_id)

    # 删除用户信息
    def delete_by_id(self, id):
        self.__user_dao.delete_by_id(id)