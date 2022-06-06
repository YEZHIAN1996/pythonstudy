from flask import Flask,render_template, make_response
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.route('/data')
def data():
    data = [
        {'id': 1,'name': 'c语言'},
        {'id': 2,'name': 'go'},
        {'id':3 ,'name': 'R'}
    ]
    response = make_response(json.dumps(data))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1234')