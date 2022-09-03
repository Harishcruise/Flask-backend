from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
# from flask_pymongo import pymongo

from Routes.routing import route_endpoint



def app():
    web_app = Flask(__name__)  # Initialize Flask App
    CORS(web_app)

    api_blueprint = Blueprint('api_blueprint', __name__)
    api_blueprint = route_endpoint(api_blueprint)

    web_app.register_blueprint(api_blueprint, url_prefix='/RestApi')    

    return web_app


app = app()

if __name__ == "__main__":
    app.run(host="localhost",debug=True)