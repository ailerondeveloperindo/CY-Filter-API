from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import classes.dependencies
import classes.classification
import classes.preprocessing
from classes.youtube_mining import *

app = Flask(__name__)
yt = Youtube("")

@app.route("/api", methods = ['GET'])
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

@app.route("/api/id=<videoid>", methods = ['GET','POST'])
def get_comments(videoid):
    return jsonify(
        videoid = videoid
    )
