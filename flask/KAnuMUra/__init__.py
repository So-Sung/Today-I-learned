from flask import Flask 

def create_app(): # ���ø����̼� ���丮 
    app = Flask(__name__)

    @app.route('/')
    def hello_flask():
        return "Welcome to Flask!!!"

    return app
# -----------------------