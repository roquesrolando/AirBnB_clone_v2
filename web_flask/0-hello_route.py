#!/usr/bin/python3
"""Starts a Flask web"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Says Hello HBNB!"""
    return ('Hello HBNB!')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
