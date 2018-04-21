from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)  #初始化Flask-Bootstrap


@app.route('/')
def index():
    return render_template('base_kid.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)  #第一个参数是模板的文件名，随后的参数都是键值对


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
