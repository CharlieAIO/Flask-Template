from flask import Flask,redirect,render_template,request,session,make_response,url_for,flash,app,send_from_directory,jsonify
from config import Config
from datetime import timedelta
import json
import pymysql
import os

app = Flask(__name__)
config_name = os.getenv("FLASK_CONFIGURATION", "Config")
app.config.from_object('config.Config')

@app.before_request
def make_session_perm():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=525600)


if __name__ == "__main__":
    app.run(debug=True)