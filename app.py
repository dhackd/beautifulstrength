from flask import Flask
from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions

import requests, jsonify
import settings

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)

api = Api(app)
api.prefix = '/api'

from endpoints.wod.resource import getWod

api.add_resource(getWod, '/wods', '/wods/<string:yymmdd>')

if __name__ == '__main__':
    app.run(host=settings.HOST,debug=True)
