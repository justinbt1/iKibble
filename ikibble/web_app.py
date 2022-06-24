#!/usr/bin/env python3

import os
from flask import Flask, render_template, url_for

template_path = os.path.abspath('../templates/')
static_path = os.path.abspath('../static/')

app = Flask(__name__, template_folder=template_path, static_folder=static_path)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
