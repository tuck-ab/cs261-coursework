import os

from flask import Flask
from flask import render_template

class WebServer:
    def __init__(self, name):
        template_dir = os.path.dirname(__file__) + "/templates"
        self.app = Flask(name, template_folder=template_dir)
        
        self.app.add_url_rule("/", "index", WebServer.index) 

    def run(self):
        self.app.run(debug="True")

    def index():
        return render_template("index.html")