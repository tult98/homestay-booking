from homestay import api
from homestay.models.models import Like, User
from flask_restplus import Resource, reqparse
from api import serializers
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims,
    get_jwt_identity
)

ns = api.namespace('api/like', description="Operations related to like")


@ns.route('/<string:user_id>')
class LikeListAPI(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth",
    params={
        "user_id": "id of user like accommodation"
    })
    @api.marshal_list_with(serializers.like)
    # @jwt_required
    def get(self, user_id):
        """"
        Return the list of like a specify user create
        <h2>Implemention Notes:</h2>
        <p> Use this method to get the list of like by a particular user
        <ul>
            <li>Send a user_id of an specify user</li>
        </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        if not (role==3 or current_id == user_id):
            return {"message": "You dont have permission"}
        user = User.find_by_id(user_id)
        if not user:
            return {"message": "Cant find the user"}
        return user.likes


@ns.route('/create')
class LikeCreateAPI(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=str, required=True)
    parser.add_argument("accommodation_id", type=str, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.expect(serializers.like)
    # @jwt_required
    def post(self):
        """
        Create a like 
        <h2>Implementation Notes:</h2>
        <p>Use this method to create a like</p>
        """
        data = self.parser.parse_args()
        like = Like(data['user_id'], data['accommodation_id'])
        like.save_to_db()
        return {"message": "Create like success"}


@ns.route('/<like_id>')
class LikeAPI(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("like_id", type=int, required=True, help="This field cannot be blank")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    # @jwt_required
    def delete(self, like_id):
        """
        Delete a like
        <h2>Implemention Notes:</h2>
        <p>Use this method to delete a like</p>
        <ul>
            <li>Send a like_id in JSOn's body</li>
        </ul
        """
        # user_id of user create the like specify like_id
        user_id = Like.get_user_id_by_like_id(like_id)
        role = get_jwt_claims()['role']
        # user_id of user currently loggin
        current_id = get_jwt_identity()
        if not (role == 3 or current_id == user_id):
            return {"message": "You dont have permission"}
        data = self.parser.parse_args()
        like = Like.find_by_id(data['like_id'])
        if not like:
            return {"message": "Cannot find that like"}
        like.delete()
        return {"message": "Delete like success"}
