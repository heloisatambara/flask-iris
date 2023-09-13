# flask-iris
A quick guide / framework to use Flask and IRIS side by side.
It follows the [Official Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/) and the [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/) as close as possible, so that you can easily use them to continue the developing of your application without conflicts.

# Installation Guide
(Optionally) Create and activate virtual environment. The following code is an example for Windows.
```
...\flask-iris> python -m venv .venv
...\flask-iris> .venv/Scripts/activate
```

1. Clone this repository
   ```
   git clone https://github.com/heloisatambara/flask-iris.git
   ```

1. Make sure you're in \flask-iris> directory on your terminal and type
   ```
   pip install -r requirements.txt
   ```



# Usage Guide
Make sure that the instance is running.

1. Edit the flaskr-iris/database.py file to connect the application to the instance where you want to store your models. The string has the format "iris://username:password@host:port/NAMESPACE". Check the [SQLAlchemy docs](https://www.sqlalchemy.org/), [this article](https://community.intersystems.com/post/sqlalchemy-easiest-way-use-python-and-sql-iriss-databases), or the [iris dialect docs](https://github.com/caretdev/sqlalchemy-iris/blob/main/README.md) for more details.
```
engine = create_engine("iris://_SYSTEM:sys@localhost:1972/SAMPLE")
```
1. Create your models on flaskr-iris/models.py, according to the [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/models/#defining-models) or [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html) Docs.

1. Run on debug mode:
```
...\flask-iris> flask --app flaskr-iris run --debug
```