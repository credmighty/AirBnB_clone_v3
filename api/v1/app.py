#!/usr/bin/python3
"""the application file"""
import storage from models
import app_views from api.v1.views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    """main function"""
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = 0.0.0.0
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
