from flask import Flask, request, redirect, render_template
#from flask_debugtoolbar import DebugToolbarExtension#\
from models import db, connect_db, User
# depicated? ==> 
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# indicate that we use postgresql and database called blogly
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#debug = DebugToolbarExtension(app)

with app.app_context() :
    connect_db(app)
    db.create_all()
    
@app.route('/')
def homepage():
    return redirect("/users")

@app.route('/users')
def list_users():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("users/index.html", users=users)

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """show list of users and hyperlink to their details to update or delete"""
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """show edit form"""
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)
    
@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """handle form submission for user's update"""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_delete(user_id):
    """handle form submission to delete user's profile"""
    
    user = User.query.get_or_404(user_id)
    
    db.session.delete(user)
    db.session.commit()
    
    return redirect('/users')

@app.route('/users/new')
def add_user():
    """show form to add new user"""
    return render_template('users/new.html')

@app.route('/users/new', methods=["POST"])
def create_user():
    """capture user's input, add to DB, and redirect to users' list page"""
    new_user = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url'] or None)
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/users')