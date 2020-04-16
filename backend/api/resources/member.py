from flask_restplus import Resource, reqparse
from homestay import bcrypt
import uuid
from homestay import api
from api import serializers
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_claims, 
    jwt_required
)
from homestay.models.models import (
    Member, 
    MemberProfile,
)

ns = api.namespace("api/member", description="Operations related to member")

@ns.route('/register')
class MemberRegisterAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('phone_number', type=str, required=True)
    parser.add_argument('password1', type=str, required=True)
    parser.add_argument('password2', type=str, required=True)
    parser.add_argument('role', type=int, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.member_register)
    def post(self):
        """
        Register a member account \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to create a new promotion</p>
            <ul>
                <li>Send a JSON object with the email, first_name, last_name, password1, password2 in the request body</li>
            </ul>
        """
        data = self.parser.parse_args()
        if Member.find_by_email(data['email']):
            return {
                'message': "This email already exist"
            }, 400

        if data['password1'] != data['password2']:
            return {
                'message': "Your confirm password doesn't match"
            }, 400
        _id = uuid.uuid4().hex
        hash_password = bcrypt.generate_password_hash(
            data['password1']).decode('utf-8')
        member = Member(_id, data['email'], hash_password, data['role'])
        member_profile = MemberProfile(
            _id, data['name'], data['phone_number'])
        member.save_to_db()
        member_profile.save_to_db()
        return {
            'message': 'create account for {} successfuly'.format(data['email'])
        }, 201


@ns.route('/login')
class MemberLoginAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.member_login)
    def post(self):
        """
        Login for member and return access token, refresh token \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to login in account</p>
        """
        data = self.parser.parse_args()
        member = Member.find_by_email(data['email'])
        if member and bcrypt.check_password_hash(member.hash_password, data['password']):
            access_token = create_access_token(identity=member)
            refresh_token = create_refresh_token(identity=member)
            return {
                "message": "loggin success",
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
        return {
            "message": "Your email or password doesnt correct"
        }


@ns.route('/')
class MemberListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.marshal_list_with(serializers.member)
    @jwt_required
    def get(self):
        """
        Return list of user account \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to get list of member account</p>
        """
        role = get_jwt_claims()['role']
        if role != 3:
            api.abort(code=400, message="You dont have permission")
        return Member.get_all_member()


@ns.route("/<string:member_id>")
class MemberAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
    params={
        "member_id": "The id for member account"
    }, security="Bearer Auth")
    @api.marshal_with(serializers.member)
    @jwt_required
    def get(self, member_id):
        """
        Return detail of a member account \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to get detail of a member account</p>
            <ul>
                <li>Specify the id of member in URL path</li>
            </ul>
        """
        role = get_jwt_claims()['role']
        if role != 3:
            api.abort(code=400, message="You dont have permisson")
        member = Member.find_by_id(_id=member_id)
        if not member:
            api.abort(code=404, message="Cannot find the account that you need")
        return member, 200
        
    
    # delete account
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={
        "member_id": "The id for user account"
    }, security="Bearer Auth")
    @jwt_required
    def delete(self, member_id):
        """
        Delete a member account of a given id \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to delete a member account of a given id</p>
            <ul>
                <li>Specify the id of user in URL path</li>
            </ul>
        """
        role = get_jwt_claims()['role']
        if role != 3:
            return {"message": "You dont have permission"}
        member = Member.find_by_id(_id=member_id)
        if member:
            member_name = member.email
            member_profile = MemberProfile.find_by_id(member_id)
            member_profile.delete()
            member.delete()
            return {"message": f"delete {member_name} account success!"}
        return {"message": "The account you need dont have in database"}
