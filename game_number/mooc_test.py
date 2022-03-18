# coding:utf-8
import sys
import datetime
import random

class Game_num(object):
    # def __init__(self):
    #     pass

    # 游戏进入提示
    def guide_page(self, guide_word):
        return '***************{}**********************'.format(guide_word)

    # 判断是否为整数
    def all_num(self, n):
        return n.isdigit()

    # 数字合法性判断函数
    def num_legal(self, ls):
        self.ls = ls
        if int(self.ls[0]) == int(self.ls[-1]):
            print('您输入的区间数字相同！！请重新启动程序。')
        elif int(self.ls[0]) > int(self.ls[-1]):
            print('您输入的数字区间大小有误！！请重新启动程序。')
        else:
            return 1
        sys.exit()

    # 产生指定区间的随机数
    def set_final_num(self, num1, num2):
        list_ = [num1, num2]
        new_list = list(filter(self.all_num, list_))

        if len(new_list) == 2:
            returnValue = self.num_legal(new_list)
            if returnValue == 1:
                print('所产生的随机数字区间为: %s' % list_)
                return random.randint(int(num1), int(num2))
        else:
            print('您所输入的为非数字字符, 请重新启动！')
            sys.exit()

    def check_num_legal(self, num):
        if int(self.ls[0]) < int(num) < int(self.ls[1]):
            return 1
        else:
            print('对不起您输入的数字未在指定区间！！！')

    def write_record(self, times, value):
        string = '第{}次您猜测的数字是{}'.format(times, value)
        now = datetime.datetime.now()
        with open('record.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{now} : {string}')

    def main(self, rand1):
        temp = 0
        while True:
            input_num = input('请继续输入您猜测的数字:')
            if self.all_num(input_num):
                input_num = int(input_num)
            else:
                print('您所输入的为非数字字符, 请重新启动！')
                sys.exit()
            if self.check_num_legal(input_num):
                continue
            temp += 1
            self.write_record(temp, input_num)
            print('*' * 10)

            if input_num < rand1:
                print('Lower than the answer')
            elif input_num > rand1:
                print('Higher than the answer')
            else:
                print('恭喜您！只用了%s次就赢得了游戏' % temp)
                break

if __name__ == '__main__':
    guess_num = Game_num()
    print(guess_num.guide_page('欢迎进入数字猜猜猜小游戏'))
    num1 = input('数字区间起始值:')
    num2 = input('数字区间终止值:')
    rand = guess_num.set_final_num(num1, num2)
    guess_num.main(rand)
