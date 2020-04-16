from flask import make_response, jsonify, abort, request
from homestay import app
from homestay.models.models import Comment
from homestay import db


@app.route('/api/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'GET':
        response_object = []
        comments = Comment.query.all()
        if not comments:
            return jsonify({'mess': 'comment is None'})
        else:
            for i in comments:
                response_object.append({
                    'id': i.id,
                    'content': i.content,
                    'user_id': i.user_id,
                    'accommodation_id': i.accommodation_id
                })
            return make_response(jsonify(response_object)), 200
    if request.method == 'POST':
        id = request.json['id']
        content = request.json['content']
        user_id = request.json['user_id']
        accommodation_id = request.json['accommodation_id']
        comment = Comment(id=id,content=content,user_id=user_id,accommodation_id=accommodation_id)
        db.session.add(comment)
        db.session.commit()
        res = {
            'id': comment.id,
            'content': comment.content,
            'user_id': comment.user_id,
            'accommodation_id': comment.accommodation_id
        }
        return jsonify(res)


@app.route('/api/comment/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def comment_id(id):
    if request.method == 'GET':
        comment = Comment.query.filter_by(id=id).first_or_404()
        if not comment:
            return jsonify({'mess': 'comment is None'})
        res = {
            'id': comment.id,
            'content': comment.content,
            'user_id': comment.user_id,
            'accommodation_id': comment.accommodation_id
        }
        return jsonify(res)
    if request.method == 'PUT':
        comment = Comment.query.filter_by(id=id).first_or_404()
        data = request.get_json()
        for i in data:
            setattr(comment, i, data[i])
        db.session.add(comment)
        db.session.commit()
        res = {
            'id': comment.id,
            'content': comment.content,
            'user_id': comment.user_id,
            'accommodation_id': comment.accommodation_id
        }
        return jsonify(res)
    if request.method == 'DELETE':
        comment = Comment.query.filter_by(id=id).first_or_404()
        if not comment:
            abort(404)
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"message": "Delete Like success"})
