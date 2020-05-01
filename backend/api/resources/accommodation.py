from flask_restplus import Resource, reqparse
from homestay.models.models import Accommodation, Member
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims,
    get_jwt_identity
)
from homestay import (
    api, 
    pagination,
)
from api import serializers
import uuid
from flask import request

ns = api.namespace('api/accommodation', description="Operations related to accommodation")

@ns.route('/create')
class AccommodationCreateAPI(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("property_type_id", type=int, required=True)
    parser.add_argument("room_type_id", type=int, required=True)
    parser.add_argument("max_guess", type=int, required=True)
    parser.add_argument("standard_guess", type=int, required=True)
    parser.add_argument("status", type=int, required=True)
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.expect(serializers.accommodation_create)
    @jwt_required
    def post(self):
        """
        Create an accommodation 
        <h2>Implemention Note: </h2>
        <p>Use this method to create an accommodation</p>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        if role == 1:
            return {"message": "You dont have permission"}
        data = self.parser.parse_args()
        _id = uuid.uuid4().hex
        if Accommodation.find_by_name(data['name']):
            return {'message': "Accommodation with that name already exist"}
        accommodation = Accommodation(id=_id,member_id=current_id, name=data['name'], property_type_id=data['property_type_id'],
                                      max_guess=data['max_guess'], room_type_id=data['room_type_id'],
                                      standard_guess=data['standard_guess'], status=data['status'])
        accommodation.save_to_db()
        return {'message': "Create accmmodation success"}

@ns.route('/search')
class AccommodationSearchAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("property_type", type=str)
    parser.add_argument("room_type", type=str)
    parser.add_argument("bed_type", type=str)
    parser.add_argument("max_guess", type=int)
    parser.add_argument("num_bathrooms", type=int)
    parser.add_argument("num_bedrooms", type=int)
    parser.add_argument("num_beds", type=int)
    # parser.add_argument("price", type=float)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.accommodation_search)
    # @api.marshal_list_with(serializers.accommodation)
    def post(self): 
        """
        Filter for accommodations 
        <h2>Implemention Note: </h2>
        <p>Use this method to filter list of accommodations</p>
        """
        data = self.parser.parse_args()
        return pagination.paginate(Accommodation.filter_accommodatons(data), serializers.accommodation)
        # return Accommodation.filter_accommodatons(data)

@ns.route('/')
class AccommodationListAPI(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}
    # , security="Bearer Auth"
    )
    # @api.marshal_list_with(serializers.accommodation)
    # @jwt_required
    def get(self):
        """
        Return the list of all accommodation have in database
        <h2>Implemention Note: </h2>
        <p>Use this method to get back the list of accommodation</p>
        """
        # role = get_jwt_claims()['role']
        # if role != 3:
        #     api.abort(code=400, message="You dont have permisson")
        return pagination.paginate(Accommodation, serializers.accommodation)

@ns.route('/member/<string:member_id>')
class AccommodationMemberListAPI(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, 
    security="Bearer Auth", 
    params={
        "member_id": "The id of member"
    })
    @api.marshal_list_with(serializers.accommodation)
    @jwt_required
    def get(self, member_id):
        """
        Return the list accommodation of a particular member
        <h2>Implemention Note: </h2>
        <p>Use this method to get back the list of accommodation for an individual</p>
        <ul>
        <li>Send the member_id in URL path</li>
        </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        member = Member.find_by_id(member_id)
        if not (role==3 or current_id==member_id):
            api.abort(code=400, messag="You dont have permission")
        else:
            if not member:
                api.abort(code=404, message="Dont have the account you need in database")
            return member.accommodations
        
@ns.route('/<string:accommodation_id>')
class AccommodationAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={
        "accommodation_id": "The id of accommodation"
    })
    @api.marshal_with(serializers.accommodation)
    def get(self, accommodation_id):
        """
        Return the detail accommodation 
        <h2>Implemention Note: </h2>
        <p>Use this method to get detail of accommodation</p>
        <ul>
        <li>Send the accommodation_id in URL path</li>
        </ul>
        """
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            api.abort(code=404, message="Cannot find the accommodation that you need")
        return accommodation

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth",
             params={
        "accommodation_id": "The id of accommodation"
    })
    @jwt_required
    def put(self, accommodation_id):
        """
        Update an accommodation
        <h2>Implemention Note: </h2>
        <p>Use this method to update an accommodation</p>
        <ul>
        <li>Send the accommodation_id in URL path</li>
        </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            api.abort(code=404, message="Cannot find the accommodation you need")
        else:
            if not (role==3 or current_id==accommodation.member_id):
                api.abort(code=400, message="You dont have permission")
            data = request.get_json()
            for field in data:
                setattr(accommodation, field, data[field])
            accommodation.save_to_db()
            return {"message": "Update the accommodation success"}

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth",
             params={
        "accommodation_id": "The id of accommodation"
    })
    @jwt_required
    def delete(self, accommodation_id):
        """
        Delete an accommodation
        <h2>Implemention Note: </h2>
        <p>Use this method to delete an accommodation</p>
        <ul>
        <li>Send the accommodation_id in URL path</li>
        </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            return {"message": "Cannot find the accommodation you need"}, 404
        else:
            if not (role==3 or current_id==accommodation.member_id):
                return {"message": "You dont have permisson"}, 400
            accommodation.delete()
            return {"message": "Delete the accommodation success"}, 200
