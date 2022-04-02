from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/marks/<marks>')
def mark(marks):
    return render_template('marks.html', marks=int(marks))


@app.route('/vals')
def vals():
    vals = request.args
    return render_template('subj.html', result=vals)


if __name__ == '__main__':
    app.run(debug=True)
