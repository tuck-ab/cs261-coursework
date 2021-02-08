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
        
        self.app.add_url_rule("/", "index", WebServer.index) 

    def run(self):
        self.app.run(debug="True")

    def index():
        return render_template("index.html")