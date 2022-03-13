import xlrd
import xlsxwriter

def read(path):
    book = xlrd.open_workbook('study.xlsx')
    data = book.sheet_by_name('学生手册')
    content = []
    for row in data.get_rows():
        row_data = []
        for j in row:
            row_data.append(j.value)
        content.append(row_data)
    return content


def write(content):
    excel = xlsxwriter.Workbook('write.xlsx')
    book = excel.add_worksheet('study')
    for index, data in enumerate(content):
        for sub_index, sub_data in enumerate(data):
            book.write(index, sub_index, sub_data)

    book1 = excel.add_worksheet('学生等级')
    data = [
        ['优秀', '良好', '中', '差'],
        [1100, 2000, 1000, 900]
    ]
    book1.write_column('A1', data[0])
    book1.write_column('B1', data[1])
    chart = excel.add_chart({'type': 'column'})
    chart.add_series({
        'categories': '=学生等级!$A1:A4',
        'values': '=学生等级!B1:B4',
        'name': '成绩占比'
    })
    chart.set_title({'name': '成绩占比图表'})
    book1.insert_chart('A10', chart)
    excel.close()


if __name__ == '__main__':
    result = read('study.xlsx')
    write(result)