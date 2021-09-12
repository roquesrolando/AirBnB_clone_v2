#!/usr/bin/python3
"""Starts a Flask web"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Says Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """Says HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """replaces _ with spaces"""

    space = text.replace("_", " ")
    return "C {}".format(space)


@app.route('/python/<text>')
def python(text='is cool'):
    """replaces _ with spaces but python"""
    space = text.replace("_", " ")
    return "Python {}".format(space)


@app.route('/number/<int:n>')
def number(n):
    """display integers"""
    if isinstance(n, int):
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """displays page if n is integer"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

