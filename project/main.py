from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/hello', methods=['POST'])
def hello():
    a = int(request.form['a'])
    b = int(request.form['b'])
    res = a*b
    return render_template('hello.html', res=res)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="80")
