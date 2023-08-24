import sqlite3
import click
from flask import current_app, g

# g is unique for each request

def init_db():
    db = get_db() # returns db connection
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        
@click.command('init-db') # now you can call init-db from command line and check this
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
    
# registers the commands
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        
        g.db.row_factory = sqlite3.Row
        
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()
        