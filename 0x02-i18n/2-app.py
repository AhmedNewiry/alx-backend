#!/usr/bin/env python3
"""
This module sets up a Flask application with Babel for internationalization (i18n).
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for Flask app.
    Includes settings for language support and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages based on the client's request.
    Returns:
        str: The best matching language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index page.
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
