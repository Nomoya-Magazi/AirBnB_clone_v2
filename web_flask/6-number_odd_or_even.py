#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """index
    Returns:
        string: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbhb
    Returns:
        string: HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """/c/<text>
    Args:
        text (string): <text> on route
    Returns:
        string: "C <text>"
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """/python/<text>
    Args:
        text (str, optional): <text>. Defaults to "is cool".
    Returns:
        str: "Python <text>"
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def intt(n):
    """/number/<int:n>
    Args:
        n (int): <int:n>
    Returns:
        str: "<int:n> is a number"
    """
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer.
    Displays the value of <n> in the body.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if <n> is an integer.
    States whether <n> is odd or even in the body.
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001', debug=False)
