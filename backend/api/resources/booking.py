from flask_restplus import Resource, reqparse
from homestay.models.models import (
    Booking,
    User,
    Member,
    Accommodation
)
from homestay import api
from api import serializers
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_claims,
    get_jwt_identity
)

ns = api.namespace('api/booking', description="Operations related to booking")

@ns.route('/')
class BookingListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.marshal_list_with(serializers.booking)
    @jwt_required
    def get(self):
        """
        Return the list of booking\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to get the list of booking</p>
        """
        role = get_jwt_claims()['role']
        if role != 3:
            api.abort(code=400, message="You dont have permission")
        return Booking.get_all_booking()


@ns.route("/user/<string:user_id>")
class BookingUserListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.marshal_list_with(serializers.booking)
    @jwt_required
    def get(self, user_id):
        """
        Return the list of booking for individual user\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to get the list of booking for individual user</p>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        user = User.find_by_id(user_id)
        if not user:
            api.abort(code=404, message="Cannot find the user you need")
        else:
            if not (role==3 or current_id==user_id):
                api.abort(code=400, message="You dont have permission")
            return user.bookings


@ns.route("/member/<string:member_id>")
class BookingMemberListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth")
    @api.marshal_list_with(serializers.booking)
    @jwt_required
    def get(self, member_id):
        """
        Return the list of booking for individual member\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to get the list of booking for individual member</p>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        member = Member.find_by_id(member_id)
        if not member:
            api.abort(code=404, message="Cannot find the member you need")
        else:
            if not (role == 3 or current_id == member_id):
                api.abort(code=400, message="You dont have permission")
            return member.bookings

@ns.route('/<string:code>')
class BookingAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
        params={
        "code": "The code of booking"
    }, security="Bearer Auth")
    @api.marshal_with(serializers.booking)
    @jwt_required
    def get(self, code):
        """
        Return detail  of a booking \n
        <h2> Implementation Notes:</h2>
        <p> Use this method to get detail of a booking\n
        <ul>
            <li>Include the code in the URL path</li>
        </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        booking = Booking.find_by_code(code)
        if booking: 
            if not (role==3 or current_id==booking.user_id or current_id==booking.member_id):
                api.abort(code=300, message="You dont have permission")
            return booking, 200
        return {
            "message": "Cannot find the booking"
        }, 400

    # @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
    #          params={"code": "The code of booking"})
    # def put(self, code):
    #     """
    #     Update a booking \n
    #     <h2> Implementation Notes:</h2>
    #     <p> Use this method to update a booking\n
    #     """
    #     booking = Booking.find_by_code(code)
    #     if booking:
    #         data = request.get_json()
    #         for field in data:
    #             setattr(booking, field, data[field])
    #         booking.save_to_db()
    #         return {
    #             "success": 1,
    #             "message": "Update your booking success"
    #         }, 200
    #     return {
    #         "success": 0,
    #         "message": "Cannot find the booking with that code"
    #     }, 400

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={"code": "The code of booking"}, security="Bearer Auth")
    @jwt_required
    def delete(self, code):
        """
        Delete a booking of a given code \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to delete a booking of a given code</p>
            <ul>
                <li>Specify the code of booking in URL path</li>
            </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        booking = Booking.find_by_code(code)
        if booking: 
            if not (role==3 or current_id==booking.member_id):
                return {"message": "You dont have permisson"}
            code_name = booking.code
            booking.delete()
            return {
                "message": f"Delete {code_name} booking success"
            }, 200
        return {
            "message": "cannot find the booking with that code"
        }, 404


@ns.route('/create/<string:accommodation_id>')
class BookingCreateAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number_of_guess', type=int, required=True)
    parser.add_argument('number_of_night', type=int, required=True)
    parser.add_argument('total_price', type=float, required=True)
    parser.add_argument('check_in', type=str, required=True)
    parser.add_argument('check_out', type=str, required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, security="Bearer Auth", 
    params={
        'accommodation_id': "The id of accommodation"
    })
    @api.expect(serializers.booking_create)
    @jwt_required
    def post(self, accommodation_id):
        """
        Create a booking \n
            <h2>Implementation Notes:</h2>
            <p>Use this method to create a new booking</p>
            <ul>
                <li>Send a JSON object with the accommodation_id, number_of_guess, number_of_night, total_price in the request body</li>
            </ul>
        """
        current_id = get_jwt_identity()
        role = get_jwt_claims()['role']
        if role != 1:
            return {"message": "You shoud not create booking"}, 400
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            return {"message": "Cannot find the accommodation you need"}, 404
        member_id = accommodation.member_id
        data = self.parser.parse_args()
        code = Booking.code_generation()
        # check if that code already exist.
        # if yes, create another code
        # if no, creat the booking
        while Booking.find_by_code(code):
            code = Booking.code_generation()
        booking = Booking(code=code, number_of_guess=data['number_of_guess'],
                          number_of_night=data['number_of_night'], total_price=data['total_price'], 
                          check_in=data['check_in'], check_out=data['check_out'],
                          member_id=member_id, user_id=current_id, accommodation_id=accommodation_id)
        booking.save_to_db()
        return {
            "message": "Create booking success"
        }, 200

