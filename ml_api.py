import pymongo
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from classes.classification import *
from classes.preprocessing import *
from classes.youtube_scraping import *

app = Flask(__name__)
#app.config['ENV'] = 'production'
#app.config['DEBUG'] = False
#app.config['TESTING'] = False

yt = Youtube_Scraping("")


@app.route("/api/", methods = ['GET'])
def ping():
    try:
        if request.get_json() is None:
            error = 400
            message = "Bad Request"
        else:
            error = 0
            message = "The API has been succesfully connected to this client"
        return jsonify(
            error = error, 
            message = message
        )
    except:
        return "404 Error"

@app.route("/api/get_detail=<videoid>", methods = ['GET','POST'])
def get_detail(videoid):
    return jsonify(
        response = yt.request_video_detail(videoid)
    )

@app.route("/api/get_comment=<videoid>&max_result=<max_result>&search_term=<search_term>", methods = ['GET','POST'])
def get_comment_SearchTerm(videoid, max_result, search_term):
    return jsonify(
        response = yt.request_comment(videoid, max_result, search_term)
    )

@app.route("/api/get_comment=<videoid>&max_result=<max_result>", methods = ['GET','POST'])
def get_comment(videoid, max_result):
    return jsonify(
        response = yt.request_comment(videoid, max_result)
    )

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

