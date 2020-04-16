from flask_restplus import Resource
from homestay.models.models import MemberProfile
from homestay import api
from flask import request
from api import serializers
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims,
    get_jwt_identity
)

ns = api.namespace("api/member_profile", description="Operations related to member profile")

@ns.route('/')
class MemberProfileListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.marshal_list_with(serializers.member_profile, skip_none=True)
    # @jwt_required
    def get(self):
        """
        Return a list of user profile \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to get the list of user profile\n
        """
        role = get_jwt_claims()['role']
        if role != 3:
            return
        return MemberProfile.get_all_profile()

@ns.route('/<string:member_id>')
class MemberProfileAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={"member_id": "The member_id of account"})
    @api.marshal_with(serializers.member_profile, skip_none=True)
    def get(self, member_id):
        """
        Return detail  of a user profile \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to get detail of a user profile\n
        """
        member_profile = MemberProfile.find_by_id(_id=member_id)
        if member_profile:
            return member_profile, 200
        else:
            return {"message": "Cannot find the account"}, 400

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={"member_id": "The member_id of account"}, security="Bearer Auth")
    # @jwt_required
    def put(self, member_id):
        """
        Update a user profile \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to update a user profile\n
        """
        _id = get_jwt_identity()
        role = get_jwt_claims()['role']
        if not (role == 3 or _id == member_id):
            return {"message": "You dont have permission"}
        member_profile = MemberProfile.find_by_id(_id=member_id)
        if member_profile:
            data = request.get_json()
            for field in data:
                setattr(member_profile, field, data[field])
            member_profile.save_to_db()
            obj_response = {"success": 1,
                            "message": "Update your profile success"
                            }, 200
        else:
            obj_response = {"success": 0,
                            "message": "Cannot find your profile"
                            }, 400
        return obj_response


