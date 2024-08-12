from flask import Flask, jsonify, request
app = Flask(_name_)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content})

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/posts', methods=['POST'])
def create_post():
    title = request.json['title']
    content = request.json['content']
    user_id = request.json['user_id']
    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'})

if _name_ == '_main_':
    app.run(debug=True)

import requests
response = requests.get('http://localhost:5000/users')
print(response.json())   
