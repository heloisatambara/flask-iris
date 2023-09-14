import os
from flask import Flask
from sqlalchemy.exc import DatabaseError

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY="dev", # override with random when deploy
        SQLALCHEMY_DATABASE_URI = "iris://_SYSTEM:sys@localhost:1972/SAMPLE"
    )
    

        
    
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
