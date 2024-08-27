#!/usr/bin/env python3
"""
0-app.py: A basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        A rendered HTML template with a welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
