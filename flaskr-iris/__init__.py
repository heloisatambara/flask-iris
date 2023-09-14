import os
from flask import Flask
from sqlalchemy.exc import DatabaseError

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
        
    
    # flask initializes Alchemy with this app
    from .database import db, engine
    from .models import User, Post
    db.init_app(app)
    try:
        with app.app_context():
            db.create_all()
    except DatabaseError as err:
        if 'already exists' in err._sql_message():
            print("Databases already exist.")
        else:
            print(err)
            
    # register blueprints
    from . import auth
    app.register_blueprint(auth.bp) 
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app
