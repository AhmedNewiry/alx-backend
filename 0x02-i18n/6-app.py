#!/usr/bin/env python3
"""
Flask app with internationalization support and user mock login.
"""

from flask import Flask, request, g, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Return a user dictionary or None if the ID cannot be found or if login_as was not passed."""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Find a user if any and set it as a global on flask.g.user."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages."""
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Locale from request headers
    locale = request.headers.get('Accept-Language')
    if locale:
        for lang in app.config['LANGUAGES']:
            if lang in locale:
                return lang

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Render the home page."""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
