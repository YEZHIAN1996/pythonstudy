import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def phone_required(form, field):
    '''手机豪验证'''
    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern, username):
        raise ValidationError
    return field
class LoginForm(FlaskForm):
    '''登陆表单'''
    username = StringField(label='用户名')
    password = PasswordField(label='密码', validators=[phone_required])
    submit = SubmitField(label='提交')

class RegisterForm(FlaskForm):
    '''用户注册表单'''
    # 默认不做csrf校验
    # def __init__(self, csrf_enabled, *args, **kwargs):
    #     super().__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    username = StringField(label='用户名')
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    birth_date = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField(label='注册')

    def validate_username(self, field):
        '''验证用户名'''
        username = field.data
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise ValidationError
        return field