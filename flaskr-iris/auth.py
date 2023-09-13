from flask import (
    Blueprint, request, g, redirect, url_for, flash, render_template, session
)
from werkzeug.security import generate_password_hash, check_password_hash
from .database import db
from .models import User
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
            
        if error is None:
            try:
                user = User(
                    username=username,
                    password=generate_password_hash(password)
                )
                
                db.session.add(user)
                db.session.commit()
            except Exception as err: # TODO: change this to sqlite3's db.IntegrityError equivalent
                error = str(err)
            else:
                return redirect(url_for("auth.login"))
        
        flash(error)
    
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        error = None
        
        try:
            user = db.one_or_404(db.select(User).where(User.username==username))
            
            if not check_password_hash(user.password, password):
                error = "Incorrect password"
        except Exception as err: # TODO also check this error
            error = f"User {username} not found."
            
        if error is None:
            session.clear()
            session['user_id'] = user.id 
            return redirect(url_for('index'))
        
        flash(error)
        
    
    return render_template('auth/login.html')
    
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = db.one_or_404(
            db.select(User).where(User.id==user_id)
        )

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view