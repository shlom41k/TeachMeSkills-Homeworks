from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


@app.route('/login')
def login():
    abort(401)  # abort(404)

    # This is never executed
    return "bla-bla-bla"


@app.errorhandler(401)
def not_found(error):
    return "OOOooopppssss", 401


if __name__ == '__main__':
    app.run(debug=True)

