import os
import json

from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_socketio import SocketIO, emit

import classes



app = Flask(__name__)
app.config["SECRET_KEY"] = "SecretKey"

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

controller = classes.Controller()


## -- Mapping pages

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["GET","POST"])
def create_meeting():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        ## -- Make new meeting
        new_meeting = controller.create_meeting()

        ## -- Send the response with token
        resp = make_response(redirect(url_for("host_page")))
        resp.set_cookie("meeting_token", new_meeting.host_token)
        return resp

@app.route("/join", methods=["POST"])
def join_meeting():
    ## -- redirect to attendee page using code as jintja parameter
    code = request.form["meetingCode"]

    return redirect(url_for("attendee_page", code=code))

@app.route("/meeting/host")
def host_page():
    return render_template("host.html") 

@app.route("/meeting/attendee/<code>")
def attendee_page(code):
    return render_template("attendee.html", meeting_code=code)


## -- Web Socket functions

@socketio.on("connect")
def connected():
    emit("connection_response", "connected")

@socketio.on("connect_as_host")
def host_connect(data):
    cookie = data["cookie"]
    meeting = controller.get_meeting_from_token(cookie)
    emit("meeting_details", {"meeting_code":meeting.code})

## -- Running the server
if __name__ == "__main__":
    socketio.run(app)