# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name_page>')
def pages(name_page):
    return render_template(name_page)


if __name__ == '__main__':
    app.run(debug=True)
