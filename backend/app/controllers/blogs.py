from . import blog_bp
from flask import jsonify, request
from app.models.blog import Blog
from app.models.user import User
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

@blog_bp.route('/addblog', methods=['POST'])
@jwt_required()
def add_blog():
    data = request.json

    # Validate required fields
    if not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Title and content are required'}), 400

    # Get the current user ID from JWT token
    user_id = get_jwt_identity()

    # Create a new blog and associate it with the logged-in user
    blog = Blog(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(blog)
    db.session.commit()

    return jsonify({
        'message': 'Blog added successfully',
        'blog': {
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'user_id': blog.user_id
        }
    }), 201


@blog_bp.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.all()
    blog_list = []
    for blog in blogs:
        blog_list.append({
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'user_id': blog.user_id,
            'username': blog.user.username,  # Access username from the related User model
            'user_obj': {
                'id': blog.user.id,
                'username': blog.user.username,
                'email': blog.user.email
            }
        })
    return jsonify(blog_list)


@blog_bp.route('/editblog/<int:blog_id>', methods=['POST'])
@jwt_required()
def edit_blog(blog_id):
    data = request.json
    print(data)
    updatetionStatus = False
    fetchedblog = Blog.query.get(blog_id)
    if(data.get('title')):
        fetchedblog.title = data['title']
        updatetionStatus = True
    if(data.get('content')):
        fetchedblog.content = data['content']
        updatetionStatus = True
    if(updatetionStatus):
        db.session.commit()
        return jsonify({'message': 'Blog updated successfully', "updatetionStatus": updatetionStatus, "updatedBlog": {
            'id': fetchedblog.id,
            'title': fetchedblog.title,
            'content': fetchedblog.content,
            'user_id': fetchedblog.user_id,
            'username': fetchedblog.user.username,  # Access username from the related User model
            'user_obj': {
                'id': fetchedblog.user.id,
                'username': fetchedblog.user.username,
                'email': fetchedblog.user.email
            }
        }})
    else:
        return jsonify({'message': 'Blog does not updated', "updatetionStatus": updatetionStatus, "updatedBlog": {
            'id': fetchedblog.id,
            'title': fetchedblog.title,
            'content': fetchedblog.content,
            'user_id': fetchedblog.user_id,
            'username': fetchedblog.user.username,  # Access username from the related User model
            'user_obj': {
                'id': fetchedblog.user.id,
                'username': fetchedblog.user.username,
                'email': fetchedblog.user.email
            }
        }})
