from flask import Blueprint, jsonify
from controller.youtube import Youtube


api_blueprint = Blueprint('api_blueprint', __name__)
yt = Youtube()

@api_blueprint.route("/api/", methods = ['GET'])
def ping():
    return jsonify(
        error = "400",
        response = "Bad Request"
    )

@api_blueprint.route("/api/get_detail=<videoid>", methods = ['GET','POST'])
def get_detail(videoid):
    return jsonify(
        response = yt.request_video_detail(videoid)
    )

@api_blueprint.route("/api/get_comment=<videoid>&max_result=<max_result>&search_term=<search_term>", methods = ['GET','POST'])
def get_comment_SearchTerm(videoid, max_result, search_term):
    return jsonify(
        response = yt.request_comment(videoid, max_result, search_term)
    )

@api_blueprint.route("/api/get_comment=<videoid>&max_result=<max_result>", methods = ['GET','POST'])
def get_comment(videoid, max_result):
    return jsonify(
        response = yt.request_comment(videoid, max_result)
    )