from homestay.models.models import Comment, Accommodation
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims,
    get_jwt_identity
)
from flask_restplus import Resource, reqparse
from homestay import api
from api import serializers
import datetime

ns = api.namespace('api/comment', description="Operations related to comment")

@ns.route('/<string:accommodation_id>')
class CommentListAPI(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("content", type=str)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.marshal_list_with(serializers.comment)
    def get(self, accommodation_id):
        """
        Return the list comment belong to an accommodation
        """
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            api.abort(code=404, message="Cannot find the acccommodation you need")
        return accommodation.comments

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.comment)
    def post(self, accommodation_id):
        """
        Create a comment in an accommodation
        """
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            return {"message": "Cannot found the accommodation you need"}, 404
        data = self.parser.parse_args()
        current_id = get_jwt_identity()
        comment = Comment(user_id=current_id,
                          accommodation_id=accommodation_id, content=data['content'])
        comment.save_to_db()
    
@ns.route('/<comment_id>')
class CommentAPI(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("content", type=str)
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth", 
    params={
        "comment_id": "The id of comment"
    })
    # @jwt_required
    def put(self, comment_id):
        """
        Update content of comment for given comment_id
        """
        current_id = get_jwt_identity()
        comment = Comment.find_by_id(comment_id)
        if not comment:
            return {"message": "Cannot find your comment"}, 404
        else:
            if current_id != comment.user_id:
                return {"message": "You dont have permission"}
                data = self.parser.parse_args()
                updated_at = datetime.datetime.now()
                comment.content = data['content']
                comment.updated_at = updated_at
                comment.save_to_db()
                return {"message": "Update comment success"}
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    # @jwt_required
    def delete(self, comment_id):
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        comment = Comment.find_by_id(comment_id)
        if not comment:
            return {"message": "Cannot find your comment"}
        else:
            if current_id != comment.user_id:
                return {"message": "You dont have permission"}
            comment.delete()
            return {"message": "Delete the comment success"}
