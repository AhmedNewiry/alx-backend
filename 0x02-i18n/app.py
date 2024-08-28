#!/usr/bin/env python3
"""
Flask app with timezone support and current time display.
"""

from flask import Flask, request, g, render_template
from flask_babel import Babel, _
import pytz
from pytz import UnknownTimeZoneError
from datetime import datetime

app = Flask(__name__)


class Config:
    """Config class for Flask app."""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieve user based on login_as parameter."""
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        return user
    return None


@app.before_request
def before_request():
    """Before request handler."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Select the best locale based on URL parameter,
    user settings, and request headers."""
    locale_param = request.args.get('locale')
    supported_locales = app.config['LANGUAGES']
    if locale_param and locale_param in supported_locales:
        return request.args['locale']
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Select the best timezone based on URL
    parameter, user settings, and default."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass
    return app.config['TIMEZONE']


@app.route('/')
def index():
    """Render the home page with current time in the inferred timezone."""
    timezone = get_timezone()
    now = datetime.now(pytz.timezone(timezone))
    # Default format: Jan 21, 2020, 5:55:39 AM
    current_time = now.strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run()
