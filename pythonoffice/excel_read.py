import xlrd

book = xlrd.open_workbook('study.xlsx')

b1 = book.sheet_by_name('学生手册')
b2 = book.sheet_by_index(0)
print(b1, b2.name)

b3 = book.sheets()

print(b1.nrows)
print(b1.ncols)

for row in b1.get_rows():
    content = []
    for j in row:
        content.append(j.value)
    print(content)