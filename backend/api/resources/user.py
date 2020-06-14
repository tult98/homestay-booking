from homestay.models.models import (User, 
                                    UserProfile, 
                                    )
from flask_restplus import Resource, reqparse
from homestay import bcrypt
import uuid
from homestay import api
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required, 
    get_jwt_claims
)
from api import serializers
from flask import jsonify
import re 

ns = api.namespace('api/user', description="Operations related to user")

@ns.route('/register')
class UserRegisterAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('first_name', type=str, required=True)
    parser.add_argument('last_name', type=str, required=True)
    parser.add_argument('phone_number', type=str, required=True)
    parser.add_argument('password1', type=str, required=True)
    parser.add_argument('password2', type=str, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.user_register)
    def post(self):
        """
        Register a user account \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to create a new user</p>
            <ul>
                <li>Send a JSON object with the email, first_name, last_name, password1, password2 in the request body</li>
            </ul>
        """
        data = self.parser.parse_args()
        if User.find_by_email(data['email']):
            return {
                'message': "This email already exist"
            }, 400
        if data['password1'] != data['password2']:
            return {
                'message': "Your confirm password doesn't match"
            }, 400
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex_pass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,40}$'
        if (len(data['email']) >=8) and (len(data['email']) <=40): 
            if not re.search(regex,data['email']):
                return {
                    "message": "Invalid Email"
                }, 400
            
            elif not re.search(regex_pass, data['password1']):
                return {
                    "message": "Password must contain at least 1 uppercase, letter and 1 special character"
                }, 400
            _id = uuid.uuid4().hex
            hash_password = bcrypt.generate_password_hash(data['password1']).decode('utf-8')
            user = User(_id, data['email'], hash_password)
            user_proflie = UserProfile(_id, data['first_name'], data['last_name'], data['phone_number'])
            user.save_to_db()
            user_proflie.save_to_db()
            return  {
                'message': 'Create account successfuly'.format(data['email'])
            }, 201
        else:
            return {
                "message": "Email must have at least 8-40 characters"
            }, 400


@ns.route("/")
class UserListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.marshal_list_with(serializers.user)
    @jwt_required
    def get(self):
        """
        Return a list of user \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to get the list of user\n
        """
        role = get_jwt_claims()['role']
        if role != 3:
            api.abort(code=400, message="You dont have permission")
        else:
            return User.get_all_users()


@ns.route('/login')    
class UserLoginAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.user_login)
    # @api.marshal_with(serializers.user)
    def post(self):
        """
        Login for user and return access token, refresh token \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to login in account</p>
        """
        data = self.parser.parse_args()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (len(data['email']) and len(data['password']) >=8) and (len(data['email']) and len(data['password']) <=40): 
            if not re.search(regex,data['email']):
                return {
                    "message": "Invalid Email"
                }, 400
            user = User.find_by_email(data['email'])
            if user and bcrypt.check_password_hash(user.hash_password, data['password']):
                access_token = create_access_token(user)
                refresh_token = create_refresh_token(user)
                return {
                    "user": user.serializer,
                    "message": "loggin success",
                    "jwt": access_token,
                    "refresh_token": refresh_token
                }, 200
            return {
                "message": "Your email or your password didn't correct"
            }, 400
        
        else:
            return {
                "message": "At least 8-40 characters"
            }, 400


@ns.route('/<string:user_id>')
class UserAPI(Resource):
    # get
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
    params={
        "user_id": "The id of user account"
    }, security="Bearer Auth")
    @api.marshal_with(serializers.user)
    @jwt_required
    def get(self, user_id):
        """
        Return detail of a user account \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to get detail of a user account</p>
            <ul>
                <li>Specify the user_id of user in URL path</li>
            </ul>
        """
        role = get_jwt_claims()['role']
        if role != 3:
            api.abort(code=400, message="You dont have permission") 
        else:
            user = User.find_by_id(_id=user_id)
            if user:
                return user, 200
            return {"message": "Cannot find the account that you need"}, 400

    # delete     
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={
        "user_id": "The user id of user account"
    }, security="Bearer Auth")
    @jwt_required
    def delete(self, user_id):
        """
        Delete a user account of a given id \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to delete a user account of a given user id</p>
            <ul>
                <li>Specify the id of user in URL path</li>
            </ul>
        """
        role = get_jwt_claims()['role']
        if role != 3:
            return {
                "message": "You dont have permission"
            }
        else:
            user = User.find_by_id(_id=user_id)
            if user:
                user_name = user.email
                user_id = user.id
                user_profile = UserProfile.find_by_id(user_id)
                user_profile.delete()
                user.delete()
                return {"message": f"Delete {user_name} account success"}, 200
            return {"message": "Dont have the account you need in database"}, 400

