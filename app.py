from flask import Flask, json

import math

app = Flask(__name__)


@app.route('/')
def default_page():
    return 'You can calculate the factorial of a non-negative integer on this app'


@app.route('/number/<int:n>')
def factorial(n):
    response = app.response_class(
        response=json.dumps(math.factorial(n)),
        status=200,
        mimetype='application/json'
    )
    return response
