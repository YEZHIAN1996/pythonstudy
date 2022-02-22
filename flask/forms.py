from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField

class LoginForm(FlaskForm):
    '''登陆表单'''
    username = StringField(label='用户名')
    password = PasswordField(label='密码')
    submit = SubmitField(label='提交')

class RegisterForm(FlaskForm):
    '''用户注册表单'''
    # 默认不做csrf校验
    # def __init__(self, csrf_enabled, *args, **kwargs):
    #     super().__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    username = StringField(label='用户名')
    password = PasswordField(label='密码')
    birth_date = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField(label='注册')
