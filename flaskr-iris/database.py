from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from sqlalchemy import create_engine
import click

engine = create_engine("iris://_SYSTEM:sys@localhost:1972/SAMPLE")
db = SQLAlchemy()
        
def drop_db():
    with current_app.app_context():
        db.drop_all()