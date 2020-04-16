from flask_restplus import Resource, reqparse
from homestay import api
from homestay.models.models import (
    Promotion,
    Member,
    Accommodation
)
from flask import request
from api import serializers
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims

ns = api.namespace('api/promotion', description='Operations related to promotion')

@ns.route('/member/<string:member_id>')
class PromotionListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth",
    params={
        "member_id": "specify id of a member"
    })
    @api.marshal_list_with(serializers.promotion)
    # @jwt_required
    def get(self, member_id):
        """
        Return the list of promotion belong to particular member\n
        <h2>Implementation Notes:</h2>\n
        Use this method to get all the promotion of a member
        """
        role = get_jwt_claims()['role']
        if role == 1:
            api.abort(code=400, message="You dont have permission")
        member = Member.find_by_id(_id=member_id)
        if not member:
            api.abort(code=404, message="Cannot find the member user you need")
        return member.promotions


@ns.route('/create')
class PromotionCreateAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("code", type=str, required=True)
    parser.add_argument('accommodation_id', type=int, required=True)
    parser.add_argument("discount_amount", type=float, required=True)
    parser.add_argument("start_time", type=str, required=True)
    parser.add_argument("end_time", type=str, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.expect(serializers.promotion)
    # @jwt_required
    def post(self):
        """
        Create a promotion\n
            <h2>Implementation Notes:</h2>
            <p>Use this method to create a new promotion</p>
            <ul>
                <li>Send a JSON object with the new code, discount_amount and start_at and end_at in the request body</li>
            </ul>
        """
        # get the id and role of current user
        data = self.parser.parse_args()
        current_id = get_jwt_identity()
        role = get_jwt_claims()['role']
        accommodation = Accommodation.find_by_id(data['accommodation_id'])
        if not accommodation:
            api.abort(code=404, message="Cannot find the accommodation you need")
        member_id = accommodation.member_id
        if not (role == 3 or current_id == member_id):
            api.abort(code=400, message="You dont have permission")
        if Promotion.find_by_code(data['code']):
            api.abort(code=400, message="The promotion with that code already exist")
        promotion = Promotion(member_id=current_id, accommodation_id=data['accommodation_id'], code=data['code'],
                              discount_amount=data['discount_amount'], start_time=data['start_time'], end_time=data['end_time'])
        promotion.save_to_db()
        return {"message": "Create promotion success"}, 200


@ns.route('/<string:code>')
class PromotionAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth",
             params={
        'code': 'Specify code associated with the promotion'
    })
    @api.marshal_with(serializers.promotion)
    def get(self, code):
        """
        Return detail of a promotion with a given code\n
        <h2>Implementation Note:</h2>\n
        Use this method to get detail of a promotion with a given code
        <ul>
            <li>Specify the Code of the promotion to get in the request URL path</li>
        </ul>
        """
        promotion = Promotion.find_by_code(code=code)
        if not promotion:
            api.abort(code=400, message="Cannot find the promotion you need")
        return promotion
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={
                 'code': 'Specify code associated with the promotion'
             }, security = "Bearer Auth")
    # @jwt_required
    def put(self, code):
        """
        Update a promotion\n
        <h2>Implementation Notes:</h2>
        Use this method to update a promotion with a given code \n
        <ul>
            <li>Send a JSON object with the new discount_amount or check_in_time in the request body</li>
            <li>Specify the Code of the promotion to get in the request URL path</li>
        </ul>
        """
        promotion = Promotion.find_by_code(code=code)
        if not promotion:
            api.abort(code=404, message="Cannot find the promotion that you need")
        member_id = promotion.member_id
        current_id = get_jwt_identity()
        role = get_jwt_claims()['role']
        if not (role == 3 or current_id == member_id):
            api.abort(code=400, message="You dont have permission")
        data = request.get_json()
        for field in data:
            setattr(promotion, field, data[field])
        promotion.save_to_db()
        return {
            "message": "update your promotion success"
        }, 200

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={
                 'code': 'Specify code associated with the promotion'
    }, security="Bearer Auth")
    # @jwt_required
    def delete(self, code):
        """
        Delete a promotion with a given code\n
        <h2>Implementation Note:</h2>\n
        Use this method to delete a promotion with a given code
        <ul>
            <li>Specify the Code of the promotion to get in the request URL path</li>
        </ul>
        """
        promotion = Promotion.find_by_code(code=code)
        if not promotion:
            api.abort(code=404, message="Cannot find the promotion you need")
        member_id = promotion.member_id
        current_id = get_jwt_identity()
        role = get_jwt_claims()['role']
        if not (role == 3 or current_id == member_id):
            api.abort(code=400, messag="You dont have permisson")
        promotion.delete()
        return {"message": "Promotion was deleted"}, 200
