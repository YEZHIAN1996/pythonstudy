# coding:utf-8
# 节省时间就没写注释，代码已上传个人git上

from example import Course, Teacher, Student

def introduction(str):
    return '****************{}*******************'.format(str)

def prepare_course():
    courses_dict = {'01': '网络爬虫', '02': '数据分析', '03': '人工智能',
                    '04': '机器学习', '05': '云计算', '06': '大数据',
                    '07': '图像识别', '08': 'Web开发'}
    course_list = []
    for key, value in courses_dict.items():
        course = Course(key, value)
        course_list.append(course)
    return course_list

def create_teacher():
    teacher_list = []
    tno = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8']
    tname = ['张亮', '王朋', '李旭', '黄国发', '周勤', '谢富顺', '贾教师', '杨教师']
    tphone = ['13301122001', '13301122002', '13301122003', '13301122004',
              '13301122005', '13301122006', '13301122007', '13301122008']
    for i in range(len(tno)):
        teacher = Teacher(tno[i], tname[i], tphone[i])
        teacher_list.append(teacher)
    return teacher_list

def course_to_teacher():
    list = []
    is_course = prepare_course()
    is_teacher = create_teacher()
    is_teacher.reverse()

    for i in range(len(is_course)):
        index = is_course[i]
        teacher_name = is_teacher[i]
        result = index.binding(teacher=teacher_name)
        list.append(result)
    return list

def create_student():
    student_name_list = ['小亮', '小明', '李红', '小丽', 'Jone', '小彤', '小K', '慕慕']
    student_name_list.reverse()
    sno_list = [sno for sno in range(1000, 1008, 1)]
    student = []
    for i in range(len(student_name_list)):
        is_student = Student(sno=sno_list[i], sname=student_name_list[i])
        student.append(is_student)
    return student

if __name__ == '__main__':
    course_to_teacher()
    students = create_student()
    c_to_t = course_to_teacher()
    # print(c_to_t)
    print(introduction('慕课学院（1）班学生信息'))
    for i in students:
        print(f'Name:{i.sname},s_number:{i.sno}')
        print(i)
    print(introduction("慕课学院（1）班选课结果"))

    for i in range(len(students)):
        # print(c_to_t[i])
        students[i].add_course(cour_info=c_to_t[i])
        print(students[i].course_detail)
        # print(students[i].course)

