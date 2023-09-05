from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine("iris://_SYSTEM:sys@localhost:1972/SAMPLE")
db = SQLAlchemy()
        