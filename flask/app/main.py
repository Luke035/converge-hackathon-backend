# coding=utf-8

from flask import render_template, abort, flash, redirect, session, url_for, request, g, Markup
import json
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.5 (default)"


@app.route('/score', methods=['POST'])
def parse_request():
    if not request.json:
        abort(400)
    print(request.json)
    return json.dumps(request.json)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
