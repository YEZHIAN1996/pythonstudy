# 温度转换实例
TmpStr = input("请输入带有符号的温度值：")
if TmpStr[-1] in ['f', 'F']:
    C = (eval(TmpStr[0:-1])-32)/1.8  # eval评估函数 去掉里面最外层的引号
    print("转换后的温度是{:.2f}C".format(C))
elif TmpStr[-1] in ['c', 'C']:
    F = 1.8 * eval(TmpStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")