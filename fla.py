from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)



@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f'Hello, {username}!'


@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/goodbye')
def goodbye():
    return 'Goodbye, Flask!'