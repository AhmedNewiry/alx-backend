#!/usr/bin/env python3
"""
Flask app that uses Babel for i18n (internationalization)
with English and French translations.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """Configuration for Babel and supported languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the index page with localized messages."""
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(debug=True)
