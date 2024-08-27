from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def index():
    n = random.randint(0, 1000)
    k = random.randint(0, 1000)
    return render_template('index.html', n=n, k=k)


@app.route('/<user>')
def index_user(user):
    return render_template('index.html', name=user)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/add_article')
def add_article():
    return  render_template('add_article.html')


@app.route('/explore')
def explore():
    links = ['Назва 1 посилання',
            'Назва 2 посилання',
            'Назва 2 посилання']

    return render_template('articles.html', links=links)


@app.route('/Details')
def Details():
    return render_template('details.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/hello/<name>')
def hello_user(name):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

