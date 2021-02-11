import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

import classes

## -- Mapping pages

app = Flask(__name__)
app.config["SECRET_KEY"] = "SecretKey"

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create_meeting():
    return render_template("create.html")

@app.route("/join")
def join_meeting():
    ## -- redirect to attendee page using code as jintja parameter
    pass

@app.route("/meeting")
def host_page():
    return render_template("host.html") 

def attendee_page():
    return render_template("attendee.html")


## -- Web Socket functions

@socketio.on("connect")
def connected():
    print("recieved")
    
    emit("connection_response", {"msg":"response recorded"})

if __name__ == "__main__":
    socketio.run(app)