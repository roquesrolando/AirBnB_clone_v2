#!/usr/bin/python3
"""Starts a Flask web"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Says Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def index():
    """Says HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

