from flask import Flask,request,redirect

app = Flask(__name__)
@app.route('/login', methods=['get'])
def login():
    if request.form['username'] == 'bill' and request.form['password'] == '1234' and request.form.get('nonce') == '87453214':
        return redirect('/static/success.html')
    else:
        return redirect('/static/failed.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')