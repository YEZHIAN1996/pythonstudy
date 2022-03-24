# coding:utf-8

from functools import reduce
# name = input('请输入用户名：')
# password = input('请输入密码：')
# print(f'用户名:{name}')
# print(f'密码：{password}')
# print(f'密码长度：{len(password)}')
# print(f'密码的数据类型{type(password)}')

# list=[100,94,98,95,97,66,87,85,79,99,92,88,98.5,95,100,77,69,86,97,79,97,99,95,66,95,98,95.5,88.5]
# print('一共有%s名学生'%len(list))
# print('最高分：%s'%max(list))
# print('最低分：%s'%min(list))


# # 以学生的姓名作为key，各科成绩作为value
# dict_1 = {'xiaomu':[95,98,99],'yanyan':[98,99,100],'xinxin':[100,97,98]}
# # dict_2以学科作为key，学生成绩作为value
# dict_2 = {'英语':[95,98,100],'语文':[98,99,97],'数学':[99,100,98]}
# print(dict_1)
# print(dict_2)

# money = [28.5,55,38,26,38]
# sum_money = sum(money)
# avg_money = sum_money / len(money)
# max_min = max(money) - min(money)
# print(f'平均值：{avg_money},最高额和最低额差值:{max_min}')


# chicken_rice = 20.5
# squid_rice = 23.5
# egg_soup = 2
# beef_soup = 2
# rice_noodles = 16
# orange_juice = 15
# strawberry = 20
# apple_juice = 15
# watermelon_juice = 20
# print("鱿鱼饭比鸡肉饭贵：", squid_rice > chicken_rice)
# print("酸菜米线比鸡肉饭便宜：", rice_noodles < chicken_rice)
# print("番茄鸡蛋汤与牛肉价格相等：", egg_soup == beef_soup)
# print("鸡肉饭的价格不等于鱿鱼饭：", chicken_rice != squid_rice)
# print("草莓汁比橙汁贵：", strawberry > orange_juice)
# print("草莓汁与西瓜汁的价格相等：", strawberry == watermelon_juice)
# print("橙汁的价格比草莓便宜：", orange_juice < strawberry)
# print("草莓汁的价格与西瓜汁的价格相等：", strawberry == watermelon_juice)

# a = 1.23-2.23
# print(type(a),id(a))
# print(min('今天是3月21号weekday'))
# print(bool(0.001))

# 迭代器
# iter_obj=iter([1,2,3])
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
#
# def test():
#     for i in range(10):
#         yield i
# res = test()
# print(next(res))
# print(next(res))
#
# # 这种迭代器不会报错
# res_1 = (i for i in [1,2,3])
# print(next(res_1))
# print(next(res_1))
# print(next(res))
# print(next(res))


# res = filter(lambda x:x>1,[0,1,2,-1])
# print(next(res))
# # print(next(res))
#
# res = map(lambda x:x>1,[0,1,2,-1])
# print(next(res))
# print(next(res))
# print(next(res))
#
# reduce_result = reduce(lambda x,y:x+y,[1,22,4])
# print(reduce_result)

# idcard = '110724200805062216'
# print(idcard[6:14])

# vote_list = ['小慕', '燕燕', '小明', '安安', '小欣', '燕燕', '小明', '燕燕', '小慕', '小明',
#              '小欣', '燕燕', '燕燕', '小慕', '小明', '安安', '小慕', '小欣', '燕燕', '小慕',
#              '小慕', '小明', '小欣', '燕燕']
# print('小慕的票数:%s'%vote_list.count('小慕'))
# print('燕燕的票数:%s'%vote_list.count('燕燕'))
# print('小明的票数:%s'%vote_list.count('小明'))
# print('安安的票数:%s'%vote_list.count('安安'))
# print('小欣的票数:%s'%vote_list.count('小欣'))

# player1 = [99, 96, 97.5, 89, 95.5, 93, 99, 95, 98, 99.5]
# player2 = [91, 95.5, 97, 92, 99, 98, 94, 95.5, 96, 99]
# player3 = [90.5, 92, 99, 99.5, 95, 90, 97, 96, 93, 91.5]
# player4 = [98, 95, 95.5, 99, 92, 93.5, 93, 97.5, 96, 99.5]
# player5 = [95, 91.5, 93, 9698.5, 99, 94, 96.5, 95.5, 92]
#
# player1.remove(max(player1))
# player1.remove(min(player1))
# player2.remove(max(player2))
# player2.remove(min(player2))
# player3.remove(max(player3))
# player3.remove(min(player3))
# player4.remove(max(player4))
# player4.remove(min(player4))
# player5.remove(max(player5))
# player5.remove(min(player5))
# avg_1 = sum(player1)/8
# avg_2 = sum(player2)/8
# avg_3 = sum(player3)/8
# avg_4 = sum(player4)/8
# avg_5 = sum(player5)/8
# list_avg = [avg_1,avg_2,avg_3,avg_4,avg_5]
# list_avg.sort(reverse=True)
# def print_avg():
#     for i in range(len(list_avg)):
#         print('第%s名，平均分为：%s'%(i+1,list_avg[i]))
# print_avg()

# coding:utf-8

# # 全体员工名单表
# staff_list = [
#     ['燕燕', '小洁', '阿楠', '小欣', '辰辰', '小浩'],  # 技术部
#     ['小美', '威威', 'Letty', 'Sophia'],  # 测试部
#     ['萌萌', '飞飞', '小刚', '佰佰'],  # 产品部
#     ['Tom', '小慕'],  # 行政部
#     ['铭铭', 'Lily'],  # 财务部
#     ['天天', '小晴']  # 人力资源部
# ]
#
# staff_list_2 = staff_list.copy()
#
# staff_list[2].append('Linda')
# staff_list[0].append('琳琳')
# staff_list[0].remove('小洁')
# staff_list[0].remove('辰辰')
# staff_list[1].remove('Letty')
#
# print('小慕的全体员工名单表：{}'.format(staff_list))
# print('人力资源部门的全体员工名单表：{}'.format(staff_list_2))

# code = ["e_ying", "d_shi", 6, "a_wo", 1, 2, 3, "f_xiong", "b_men", 4, 5, "c_dou"]
# # 定一个空列表crack 放入字符串
# crack = []
# # 定义一个空列表number 放入数字
# number= []
# # 使用append将code里面的字符串根据索引添加到crack列表中
# crack.append(code[0])
# crack.append(code[1])
# crack.append(code[3])
# crack.append(code[7])
# crack.append(code[8])
# crack.append(code[11])
# print("字符串添加完成", crack)
# # 使用append将code里面的数字根据索引添加到number列表中
# number.append(code[2])
# number.append(code[4])
# number.append(code[5])
# number.append(code[6])
# number.append(code[9])
# number.append(code[10])
# print("数字添加完成", number)
# # 使用sort对crack和number列表进行排序
# crack.sort()
# number.sort()
# print("新字符串列表排序", crack, "\n", "新数字列表排序", number)
# # 使用reverse对两个列表进行反序
# crack.reverse()
# number.reverse()
# print("反转后的新字符串列表crack", crack)
# print("反转后的新数字列表number", number)
# # 再将原列表复制了一份并且将原列表里面的内容清空
# new_code = code.copy()
# print("复制原编码", new_code)
# code.clear()
# print("清空原列表编码", code)

# mon = '周一特价%s %d元，赠送一份价值%f的%s'  # 周一活动
# tue = '周二特价%s %d元，赠送一份价值%f的%s'  # 周二活动
# wed = '周三特价%s %d元，赠送一份价值%f的%s'  # 周三活动
# thu = '周四特价%s %d元，赠送一份价值%f的%s'  # 周四活动
# fri = '周五特价%s %d元，赠送一份价值%f的%s'  # 周五活动
# activities = '{}饭店不仅每天有特价，为了回馈新老客户到店就送价值{}的精美礼品，凭结账小票可进行抽奖\n一等奖： 价值{}欧洲游\n二等奖： 价值{}的豆浆机\n三等奖： 价值{}元的生活大礼包'  # 饭店活动介绍
# mon_format = mon % ('麻辣小龙虾', 23, 9.8, '罗宋汤')
# tue_format = tue % ('宫保鸡丁', 12, 9.8, '紫菜蛋花汤')
# wed_format = wed % ('水煮肉片', 32, 9.8, '西湖牛肉羹')
# thu_format = thu % ('果儿拌菜', 19, 9.8, '番茄鸡蛋汤')
# fri_format = fri % ('小鸡炖蘑菇', 33, 9.8,'米酒小汤圆')
# activities_format = activities.format('小北', 29.9, '一万元', 388, 200)
# print(mon_format)
# print(tue_format)
# print(wed_format)
# print(thu_format)
# print(fri_format)
# print('******************************')
# print(activities_format)


# movies = {
#     "沉默的羔羊": "1991-02-14",
#     "不可饶恕": "1992-08-03",
#     "辛德勒的名单": "1993-11-30",
#     "阿甘正传": "1994-06-23",
#     "勇敢的心": "1995-05-18",
#     "英国病人": "1996-12-06",
#     "泰坦尼克号": "1997-12-19",
#     "莎翁情史": "1998-12-11",
#     "美国丽人": "1999-09-08",
#     "角斗士": "2000-05-05",
#     "美丽心灵": "2001-12-13",
#     "芝加哥": "2002-12-27",
#     "指环王：国王归来": "2003-12-17",
#     "百万美元宝贝": "2004-12-15",
#     "撞车": "2005-09-10",
#     "无间行者": "2006-09-26",
#     "老无所依": "2007-05-19",
#     "贫民窟的百万富翁": "2008-08-30",
#     "拆弹部队": "2009-09-04",
#     "国王的演讲": "2010-09-06",
#     "艺术家": "2011-10-12",
#     "逃离德黑兰": "2012-08-31",
#     "为奴十二年": "2013-11-08",
#     "鸟人": "2014-08-27",
#     "聚焦": "2015-09-03",
#     "月光男孩": "2016-09-02",
#     "水形物语": "2017-08-31",
#     "绿皮书": "2018-09-11",
#     "寄生虫": "2019-05-21",
#     "无依之地 [4]": " 2020-09-11",
# }
# names = ['肖申克的救赎','楚门的世界','泰坦尼克号']
#
# for name in names:
#     if name in movies:
#         print(name, '是奥斯卡近30年最佳影片')
#     else:
#         print(name, '是奥斯卡近30年最佳影片')


# 商品型号：库存数量
# huawei_phone = {"P20Pro": 0, "Mate30": 0, "Mate30Pro": 0}
# xiaomi_phone = {"mi5s": 0, "mi9pro": 28, "redmi9A": 19}
# nokia_phone = {"Lumia920": 0, "nokia_8110": 0}
#
# huawei_phone.clear()
# xiaomi_phone.pop('mi5s')
# del nokia_phone


# grade_one = {
#    "class_1": {"boy": 25, "gril": 22},
#    "class_2": {"boy": 21, "gril": 23},
#    "class_3": {"boy": 24, "gril": 22},
#    "class_4": {"boy": 22, "gril": 22},
#    "class_5": {"boy": 20, "gril": 25}
# }
# class_list = list(grade_one.values())
# for i in range(5):
#     print(f'一年{i+1}班:{class_list[i]}')

book_info = {
   "book_name": "English Listening Training",  # 书名
   "total_chapter": 10,                 # 总章节
   "finished_chapter": "",               # 完成章节
   "avg_score": 0,                    # 平均得分
   "wrong_ques_num": 0,                 # 错题数量
   "user_name": ""                    # 学生姓名
}
小慕完成了 8 个章节，平均得分 95.5 分，错题数量 12 道
xiaomu = book_info.copy()
tom = book_info.copy()
kate = book_info.copy()
xiaomu.update({
   "finished_chapter": 8,               # 完成章节
   "avg_score": 95.5,                    # 平均得分
   "wrong_ques_num": 12,                 # 错题数量
   "user_name": ""})
print(xiaomu,tom,kate)