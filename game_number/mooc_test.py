# coding:utf-8
import sys
import datetime
def guide_page(guide_word):
    return '***************{}**********************'.format(guide_word)

def all_num(n):
    if not n.isdigit():
        return '您输入的为非数字字符，请重新启动！'
    else:
        return n

def num_legal(ls):
    if int(ls[0]) == int(ls[1]):
        sys.exit()
        return '您输入的区间数字相同！！请重新启动程序。'
    elif int(ls[0]) > int(ls[1]):
        sys.exit()
        return '您输入的数字区间大小有误！！请重新启动程序。'
    else:
        return 1

def set_final_num(num1, num2):
    list_ = [num1, num2]
    new_list = list(filter(all_num, list_))
    # num_legal(new_list)
    return new_list



def check_num_legal(num):
    pass
def write_record(times, value):
    # now = datetime.datetime.now()
    for i in times:
        now = datetime.datetime.now()
        string = f'{now}:第{i}次您猜测的数字为：{value[i]}'
        with open('record.txt') as f:
            f.write(string, 'wb')




if __name__ == '__main__':
    print(guide_page('欢迎进入数字猜猜猜小游戏'))
    print(set_final_num(1, 2))