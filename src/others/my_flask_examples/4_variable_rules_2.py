from flask import Flask

app = Flask(__name__)


@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    # show the blog with the given id, the id is an integer
    return "Blog Number: {}".format(post_id)


@app.route('/rev/<float:rev_number>')
def revision(rev_number):
    # show the revision version, the rev is an float
    return "Revision number: {}".format(rev_number)


@app.route('/path/<path:my_path>')
def my_path_to(my_path):
    # show the subpath after /path/
    return "My path: {}".format(my_path)


if __name__ == '__main__':
    app.run(debug=True)