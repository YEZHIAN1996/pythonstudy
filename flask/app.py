import os

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm

app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:yza0404..@localhost/school'
app.config['WTF_CSRF_SECRET_KEY'] = 'abc123abc'
app.config['SECRET_KEY'] = 'abc123abc'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'weibo_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)

class UserAddress(db.Model):
    __tablename__ = 'weibo_user_addr'
    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('weibo_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/user/<int:page>/')
def list_user(page):
    '''用户分页'''
    # 1.查询用户信息
    per_page = 10 # 每一页的数据大小
    user_ls = User.query
    user_page_data = user_ls.paginate(page, per_page)
    return render_template('list_user.html', user_page_data=user_page_data)


@app.route('/form', methods=['POST', 'GET'])
def page_form():
    form = LoginForm()
    #
    if form.validate_on_submit():
        print('登录成功')
    else:
        print(form.errors)
    return render_template('page_form.html', form=form)

@app.route('/user/register', methods=['GET', 'POST'])
def page_register():
    '''新用户注册'''
    # csrf_enabled为false表示不做csrf校验 csrf_enabled=False
    form = RegisterForm()
    if form.validate_on_submit():
        # 表单验证通过
        # 1.获取表单数据
        username = form.username.data
        password = form.password.data
        birth_date = form.birth_date.data
        age = form.age.data
        # 2.构建用户对象
        user = User(
            username=username,
            password=password,
            birth_date=birth_date,
            age=age
        )
        # 3.提交到数据库
        db.session.add(user)
        db.session.commit()
        # 4.跳转到登录页面
        return redirect(url_for('hello_world'))
    else:
        print(form.errors)
    return render_template('page_register.html', form=form)

@app.route('/img/upload', methods=['GET', 'POST'])
def img_upload():
    file_path = os.path.join(os.path.dirname(__file__), 'medis')
    if request.method == 'POST':
        files = request.files
        file1 = files.get('file1', None)
        if file1:
            file_name = os.path.join(file_path, file1)
            file1.save(file_name)
        return redirect(url_for('img_upload'))
    return render_template('img_upload.html')
if __name__ == '__main__':
    app.run()
