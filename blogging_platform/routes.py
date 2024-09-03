from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Post, Comment, User

routes = Blueprint('routes', __name__)

@routes.route('/api/posts', methods=['POST'])
@jwt_required()
def create_post():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    if user.role not in ['admin', 'author']:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.json
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Missing data'}), 400

    new_post = Post(title=title, content=content, author_id=user.id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully'}), 201

@routes.route('/api/posts', methods=['GET'])
def get_posts():
    author = request.args.get('author')
    query = Post.query

    if author:
        user = User.query.filter_by(username=author).first()
        if user:
            query = query.filter_by(author_id=user.id)

    page = request.args.get('page', 1, type=int)
    posts = query.paginate(page, 2, False).items

    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author.username, 'created_at': post.created_at} for post in posts]), 200

@routes.route('/api/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    data = request.json
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Missing data'}), 400

    post = Post.query.get_or_404(post_id)
    new_comment = Comment(content=content, post_id=post.id, user_id=user.id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'message': 'Comment added successfully'}), 201
