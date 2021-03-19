import os
from flask import Flask 
from flask import render_template


def create_app(): 
    app = Flask(__name__)



    @app.route('/')
    def hello_flask():
        return render_template("Daily.html")
    @app.route('/a/')
    def Board():
        return render_template("index.html")
    @app.route('/b/')
    def About():
        return render_template("About.html")
    @app.route('/c/')
    def eAbout():
        return render_template("test.html")    
    return app
# -----------------------
