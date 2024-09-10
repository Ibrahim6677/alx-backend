#!/usr/bin/env python3
"""
This is the main file of the flask application.
"""
from flask import Flask, render_template
app = Flask(__name__)


# Define the route for the homepage
@app.route("/", strict_slashes=False)
def HomePage() -> str:
    """
    This is the main page of the flask application.
    Returns:
        str: The rendered template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
