from flask import Blueprint, redirect, url_for
from flask_cors import CORS, cross_origin

main = Blueprint('main', 'api')
cors = CORS(main, resources={r"/*": {"origins": "http://localhost:3000"}}) #Add your url of project here

@main.route('/', methods=["GET"])
@cross_origin()
def index():
    return f'<h1>Index</h1>'

@main.route('/help', methods=["GET"])
@cross_origin()
def help():
    return f'<h1>Help</h1>'

@main.route('/req', methods=["GET"])
@cross_origin()
def req():
    return f'<h1>Request</h1>'

@app.route("/check", methods=["GET"])
@cross_origin()
def check():
    return {
        "status":"ok"
    }