import os
from flask import Flask, request

# 定义服务端保存文件的位置
UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, os.path.basename(file.filename)))
        return '上传成功'

if __name__ == '__main__':
    app.run()