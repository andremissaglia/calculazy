#!/usr/bin/env python

import sys
import os
import sympy
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/<input>")
def calculate(input = ''):
    try:
        desc = ''
        title = str(sympy.simplify(input))
        return render_template('index.html', title=title, description = desc)
    except Exception as e:
        return render_template('index.html', title='Sorry :(', description = "There was an error parsing mathematical expression")

@app.route("/")
def home():
    return render_template('index.html', title='Send me an expression', description = "There's a lot of mathematical equations I can simplify for you")

if __name__ == '__main__':
    port = os.environ.get('PORT') or 8000
    app.run(port = port)