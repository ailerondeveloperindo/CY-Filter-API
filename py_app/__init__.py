import sys, os
# adds working path to sys.path
sys.path.insert(0,os.path.abspath('./py_app/'))

import json, pymongo
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from .utils.regis_blueprint import RegBlue
from .config import Config

app = Flask(__name__)
cfg = Config()
rb = RegBlue(app, cfg.Views)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

