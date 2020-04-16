from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
from homestay.models.models import RevokedTokenModel
from flask_restplus import Resource
from homestay import api
from api import serializers

ns = api.namespace('api/auth', description="Operations related to auth")

@ns.route('/')
class TokenRefresh(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.token)
    @jwt_refresh_token_required
    def post(self):
        """
        Renew access token\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to reprovide access token by refresh token</p>
        """
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


@ns.route('/access')
class LogoutAccess(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.token)
    @jwt_required
    def post(self):
        """
        Revoked access token\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to revoked access token and addition it to black list</p>
        """
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti)
            revoked_token.add()
            return {
                'jti': jti,
                'message': 'Refresh token has been revoked'
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500


@ns.route('/refresh')
class LogoutRefresh(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.token)
    @jwt_refresh_token_required
    def post(self):
        """
        Revoked refresh token\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to revoked access token and addition it to black list</p>
        """
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti)
            revoked_token.add()
            return {
                'jti': jti,
                'message': 'Refresh token has been revoked'
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500
