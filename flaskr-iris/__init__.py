import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY="dev", # override with random when deploy
        SQLALCHEMY_DATABASE_URI = "iris://_SYSTEM:sys@localhost:1972/SAMPLE"
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config is passed in
        app.config.from_mapping(test_config)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        print("instance folder doesn't exist")
    
    # test if its working
    @app.route('/')
    def hello():
        return "hello world"
    
    from .db import init_db
    with app.app_context():
        init_db(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app