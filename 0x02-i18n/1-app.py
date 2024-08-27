#!/usr/bin/env python3
"""
This module initializes a Flask application with the Flask-Babel
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Initialize Flask app
app = Flask(__name__)

# Apply the Config class to the app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@app.route('/')
def index():
    """
    Index route that returns a simple greeting.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
