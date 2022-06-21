import time
from os import system
from service.user_service import UserService
from colorama import Fore, Style

__user_service = UserService()
while True:
    system('clear')
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTBLUE_EX, "\n\t1.登陆系统")
    print(Fore.LIGHTBLUE_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号：")
