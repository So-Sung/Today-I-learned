from flask import Flask 

def create_app(): # 애플리케이션 팩토리 
    app = Flask(__name__)

    @app.route('/')
    def hello_flask():
        return "Welcome to Flask!!!"

    return app
# -----------------------