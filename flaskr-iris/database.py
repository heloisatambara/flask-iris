from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import click

db = SQLAlchemy()
        
def drop_db():
    with current_app.app_context():
        db.drop_all()