import os

from flask import Flask
from flask import render_template

class WebServer:
    def __init__(self, name):
        template_dir = os.path.dirname(__file__) + "/templates"
        static_dir = os.path.dirname(__file__) + "/static"

        self.app = Flask(name, 
                         template_folder=template_dir,
                         static_folder=static_dir,
                         static_url_path="/webserver/static",
        )
        
        self.app.add_url_rule("/", "index", index) 
        self.app.add_url_rule("/create", "create", create_meeting)
        self.app.add_url_rule("/join", "join", join_meeting, ["POST"])

        self.app.add_url_rule("/meeting", "meeting", host_page)

    def run(self):
        self.app.run(debug="True")

def index():
    return render_template("index.html")

def create_meeting():
    return render_template("create.html")

def join_meeting():
    ## -- redirect to attendee page using code as jintja parameter
    pass

def host_page():
    return render_template("host.html") 

def attendee_page():
    return render_template("attendee.html")