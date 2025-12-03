from flask import Flask

def create_app():

    # create flask app
    app = Flask(__name__)

    # define routes

    @app.route('/', methods=['GET'])
    def root():
        return "welcome to the flask application"
    
    @app.route('/health', methods=['GET'])
    def health():
        return "healthy"
    
    return app
