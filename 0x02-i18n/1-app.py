#!/usr/bin/env python3
""" A Flask Application"""


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)   # Module level variable to store Babel Object


class Config:
    """A Configuration Class to set-up default
    Language as English and timezone as UTC"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """index route to render index template"""

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
