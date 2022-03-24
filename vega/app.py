from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
import mysql

import os
import sys
import time
__user_service = UserService()
__news_service = NewsService()
while 1:
    os.system('clear')
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTBLUE_EX, "\n\t1.登陆系统")
    print(Fore.LIGHTBLUE_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号：")
    if opt=="1":
        username=input("\n\t用户名：")
        password=input("\n\t密码：")
        result = __user_service.login(username, password)
        # 登陆成功
        if result:
            role = __user_service.search_user_role(username)
            os.system("clear")
            while 1:
                if role=="新闻编辑":
                    pass
                elif role=="管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTGREEN_EX, "\n\tback.退出登陆")
                    print(Fore.LIGHTGREEN_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt=="1":
                        os.system("clear")
                        print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                        print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                        print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入操作编号：")
                        if opt=="1":
                            page = 1
                            while 1:
                                os.system("clear")
                                count_page = __news_service.search_unreview_count_page()
                                result = __news_service.search_unreview_list(page)
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (index+1, one[1], one[2], one[3]))
                                print(Fore.LIGHTBLUE_EX, "\n\t------------------")
                                print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                print(Fore.LIGHTBLUE_EX, "\n\t------------------")
                                print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入操作编号：")
                                if opt=="back":
                                    break
                                elif opt=="prev" and page>1:
                                    page-=1
                                elif opt=="next" and page<count_page:
                                    page+=1

                    elif opt=="2":
                        pass
                    elif opt=="back":
                        break
                    elif opt=="exit":
                        sys.exit(0)
        else:
            print("\n\t登陆失败(3s自动返回)")
            time.sleep(3)
    elif opt=="2":
        sys.exit(0)