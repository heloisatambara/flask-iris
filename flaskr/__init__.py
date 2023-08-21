import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', # override with random when deploy
    #    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), # CHANGE TO IRIS
        SQLALCHEMY_DATABASE_URI = "iris://_SYSTEM:SYS@localhost:1972/SAMPLE"
    ) 
  
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        print("instance folder doesn't exist")

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'
    
    # import the database created
    from flaskr.db import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app    