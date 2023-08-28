from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from .auth import login_required
from .database import db
from .models import Post
from sqlalchemy import desc

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = db.session.scalars(
        db.select(Post).order_by(desc(Post.created))
    ).all() # find equivalent to fetchall - see how it works to pass it on to the .html file
    
    return render_template('blog/index.html', posts=posts)
