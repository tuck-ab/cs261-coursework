import os

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit

import classes



app = Flask(__name__)
app.config["SECRET_KEY"] = "SecretKey"

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


## -- Mapping pages

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create_meeting():
    return render_template("create.html")

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
    print("recieved")

    emit("connection_response", {"msg":"response recorded"})



## -- Running the server
if __name__ == "__main__":
    socketio.run(app)