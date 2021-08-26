
import json, pymongo
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from helpers.register_blueprint import Register_Blueprint
from config import Config

py_app = Flask(__name__)
cfg = Config()
rb = Register_Blueprint(py_app, cfg.Views)


@py_app.errorhandler(HTTPException)
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

