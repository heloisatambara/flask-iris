from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import click


def init_db(app): 
    db = get_db() # returns db connection
    db.init_app(app)
    with current_app.app_context():
        db.create_all()
        
def drop_db():
    db = get_db() # returns db connection
    
    with current_app.app_context():
        db.drop_all()
 
        
@click.command('init-db') # now you can call init-db from command line and check this
def init_db_command():
    # clear existing data and create new tables
    
    init_db()
    click.echo("Initialized the database.")
    

# registers the commands
def init_app(app):
    app.cli.add_command(init_db_command)
    
def get_db():
    db = SQLAlchemy()
    return db