# coding: utf-8

import xlrd


class HandleExcel(object):
    def __init__(self, filename):
        self.filename = filename

    # 读取Excel表中的学生成绩
    # 以字典形式返回学生成绩，学号为字典的key，其余内容为字典的value
    # 格式：{20213301: ['慕桂英', '女', 99.0, 100.0, 96.0], 20213302: ['dewei', '男', 98.0, 95.0, 97.5], ...}
    def get_data(self):
        excel = xlrd.open_workbook(self.filename)

        book = excel.sheet_by_index(0)
        stu_dict = {}
        for row_num in range(1, book.nrows):
            k = int(book.row_values(row_num)[0])
            stu_dict[k] = book.row_values(row_num)[1:]

        return stu_dict


if __name__ == "__main__":
    d = HandleExcel("../script/students.xlsx")
    res = d.get_data()
    print(res)