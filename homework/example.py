# coding:utf-8

class Student():
    def __init__(self, sno, sname, course=[]):
        self.sno = sno
        self.sname = sname
        self.course = []

    def course_detail(self):
        return f'Name:{self.sname},selected:{self.course}'

    def add_course(self, cour_info):
            self.course.append(cour_info)

    # def str(self):
    #     return 'name:%s,s_number:%s'.format(self.sname, self.sno)


class Teacher():
    def __init__(self, tno, tname, tphone):
        self.tno = tno
        self.tname = tname
        self.tphone = tphone

    # def str(self):
    #     return f'tno:{self.tno},tname:{self.tname}'

class Course():
    def __init__(self, cno, cname, teacher=None):
        self.cno = cno
        self.cname = cname
        #self.teacher = teacher
    def binding(self, teacher):
        if teacher is not None:
            self.teacher = teacher
            return {'课程名称：{},教师名称：{}'.format(self.cname, self.teacher.tname)}
        else:
            return ''
