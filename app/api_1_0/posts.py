from . import api
from .. import auth
from flask import jsonify, url_for, request
from app.models import Post, Permission
from .. import auth
from .. import db
from ..decorators import permission_required


@api.route('/posts/')
def get_posts():
    posts = Post.query.all()
    return jsonify({'posts': [post.to_json for post in posts]})


@api.route('/posts/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json)


@api.route('/posts/', methods=['POST'])
@permission_required(Permission.WRITE_ARTICLES)
def new_post():
    post = Post.from_json(request.json)
    post.author = "hhh"
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
        {'Location': url_for('api.get_post', id=post.id, _external=True)}
