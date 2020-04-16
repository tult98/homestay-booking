from flask_restplus import Resource
from homestay.models.models import UserProfile
from homestay import api
from flask import request
from api import serializers
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity

ns = api.namespace("api/user_profile", description="Operations related to user profile")

@ns.route("/")
class UserProfileListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.marshal_list_with(serializers.user_profile, skip_none=True)
    def get(self):
        """
        Return a list of user profile \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to get the list of user profile\n
        """
        # role = get_jwt_claims()['role']
        # if role != 3:
        #     return 
        # else:
        return UserProfile.get_all_profile()


@ns.route('/<string:user_id>')
class UserProfileAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={"user_id": "The id of account"})
    @api.marshal_with(serializers.user_register)
    def get(self, user_id):
        """
        Return detail  of a user profile \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to get detail of a user profile\n
        <ul>
            <li>Include the id in the URL path</li>
        </ul>
        """
        user_profile =  UserProfile.find_by_id(_id=user_id)
        if user_profile:
            return user_profile, 200
        else:
            return {"message": "Cannot find the account"}, 400

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={"user_id": "The id of account"}, security="Bearer Auth")
    # @jwt_required
    def put(self, user_id):
        """
        Update a user profile \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to update a user profile\n
        """
        _id = get_jwt_identity()
        role = get_jwt_claims()['role']
        # if not admin or own account
        if not (role == 3 or _id == user_id):
            return {"message": "You dont have permisson"}
        else:
            user_profile = UserProfile.find_by_id(user_id)
            if user_profile:
                data = request.get_json()
                for field in data:
                    setattr(user_profile, field, data[field])
                user_profile.save_to_db()
                return {
                        "message": "Update your profile success"
                        }, 200
            return {
                    "message": "Cannot find your profile"
                    }, 400
