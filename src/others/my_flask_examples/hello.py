from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<user_name>')
def hello(user_name):
    return render_template('hello.html', name=user_name)


if __name__ == '__main__':
    app.run(debug=True)
