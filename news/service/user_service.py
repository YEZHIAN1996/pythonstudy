from news.db.user_dao import UserDao

class UserService:
    __user_service = UserDao()

    def login(self, username, password):
        return self.__user_service.login(username, password)