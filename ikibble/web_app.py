import os
import sqlite3
from flask import Flask, render_template

template_path = os.path.abspath('../templates/')
static_path = os.path.abspath('../static/')

app = Flask(__name__, template_folder=template_path, static_folder=static_path)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
