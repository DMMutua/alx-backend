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


@babel.localeselector
def get_locale():
    """Checks for Language Preference in App User System and Uses It"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """index route to render index template"""

    title = gettext('Welcome to Holberton')
    header = gettext('Hello world')
    return render_template('2-index.html', title=title, header=header)


if __name__ == '__main__':
    app.run()
