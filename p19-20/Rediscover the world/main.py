from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def index():
    n = random.randint(0, 1000)
    k = random.randint(0, 1000)
    return render_template('index.html', n=n, k=k)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/add_article')
def add_article():
    return  render_template('add_article.html')


@app.route('/explore')
def explore():
    return render_template('articles.html')


@app.route('/<name>')
def test(name):
    return f"<h1>text {name}</h1>"


if __name__ == '__main__':
    app.run(debug=True)

