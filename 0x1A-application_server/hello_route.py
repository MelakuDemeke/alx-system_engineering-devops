#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/airbnb-onepage/', methods=['GET'])
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
