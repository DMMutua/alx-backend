#!/usr/bin/env python3
""" A Flask Application"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """index route to render index template"""

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
