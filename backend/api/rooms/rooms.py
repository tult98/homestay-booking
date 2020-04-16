from flask import make_response, jsonify, abort, request
from homestay import app
from homestay.models.models import Accommodation, Price
from homestay import db
import uuid


@app.route('/api/room', methods=['GET', 'POST'])
def room():
    if request.method == 'GET':
        response_object = []
        room = Accommodation.query.all()
        for i in room:
            response_object.append({
                'data': {
                    'id': i.id,
                    'name': i.name,
                },
                'success': 1,
            })
        return make_response(jsonify(response_object)), 200
    elif request.method == 'POST':
        id = uuid.uuid4().hex
        name = request.json['name']
        address = request.json['address']
        member_id = request.json['member_id']
        description = request.json['description']
        special_notices = request.json['special_notices']
        bed_type_id = request.json['bed_type_id']
        room_type_id = request.json['room_type_id']
        property_type_id = request.json['property_type_id']
        max_guess = request.json['max_guess']
        num_bathrooms = request.json['num_bathrooms']
        num_bedrooms = request.json['num_bedrooms']
        num_beds = request.json['num_beds']
        status = request.json['status']
        apartment_manual = request.json['apartment_manual']
        apartment_rule = request.json['apartment_rule']
        checkin_guide = request.json['checkin_guide']
        accommodation_id = request.json['accommodation_id']
        additional_guess_fee = request.json['additional_guess_fee']
        cleaning_fee = request.json['cleaning_fee']
        security_fee = request.json['security_fee']
        monthly_price = request.json['monthly_price']
        nightly_price = request.json['nightly_price']
        weekend_price = request.json['weekend_price']
        cancelation_policy = request.json['cancelation_policy']
        check_in = request.json['check_in']
        check_out = request.json['check_out']
        room = Accommodation(id=id, member_id=member_id, property_type_id=property_type_id,
                             room_type_id=room_type_id, bed_type_id=bed_type_id, name=name, address=address,
                             description=description, special_notices=special_notices, status=status,
                             max_guess=max_guess, num_bathrooms=num_bathrooms, num_bedrooms=num_bedrooms,
                             num_beds=num_beds,
                             apartment_manual=apartment_manual, apartment_rule=apartment_rule,
                             checkin_guide=checkin_guide)
        price = Price(accommodation_id=accommodation_id, additional_guess_fee=additional_guess_fee,
                      cleaning_fee=cleaning_fee, security_fee=security_fee, monthly_price=monthly_price,
                      nightly_price=nightly_price, weekend_price=weekend_price, cancelation_policy=cancelation_policy,
                      check_in=check_in, check_out=check_out)
        db.session.add(room)
        db.session.add(price)
        db.session.commit()
        res = {
            'id': id,
            'name': room.name,
            'member_id': room.member_id,
            'address': room.address,
            'description': room.description,
            'special_notices': room.special_notices,
            'bed_type_id': room.bed_type_id,
            'room_type_id': room.room_type_id,
            'property_type_id': room.property_type_id,
            'max_guess': room.max_guess,
            'num_bathrooms': room.num_bathrooms,
            'num_bedrooms': room.num_bedrooms,
            'num_beds': room.num_beds,
            'status': room.status,
            'apartment_manual': room.apartment_manual,
            'apartment_rule': room.apartment_rule,
            'created_at': room.created_at,
            'accommodation_id': price.accommodation_id,
            'additional_guess_fee': price.additional_guess_fee,
            'cleaning_fee': price.cleaning_fee,
            'security_fee': price.security_fee,
            'monthly_price': price.monthly_price,
            'nightly_price': price.nightly_price,
            'weekend_price': price.weekend_price,
            'cancelation_policy': price.cancelation_policy,
            'check_in': price.check_in,
            'check_out': price.check_out
        }
        return jsonify(res)


@app.route('/api/room/<int:id>', methods=['GET', 'PUT'])
def room_id(id):
    res = {}
    if request.method == 'PUT':
        room = Accommodation.query.filter_by(id=id).first()
        data = request.get_json()
        for i in data:
            setattr(room, i, data[i])
        db.session.add(room)
        db.session.commit()
        res = {
            'id': id,
            'name': room.name,
            'member_id': room.member_id,
            'address': room.address,
            'description': room.description,
            'special_notices': room.special_notices,
            'bed_type_id': room.bed_type_id,
            'room_type_id': room.room_type_id,
            'property_type_id': room.property_type_id,
            'max_guess': room.max_guess,
            'num_bathrooms': room.num_bathrooms,
            'num_bedrooms': room.num_bedrooms,
            'num_beds': room.num_beds,
            'status': room.status,
            'apartment_manual': room.apartment_manual,
            'apartment_rule': room.apartment_rule,
            'created_at': room.created_at
        }
    elif request.method == 'GET':
        room = Accommodation.query.filter_by(id=id).first_or_404()
        if not room:
            abort(404)
        res = {
            'id': room.id,
            'name': room.name,
            'member_id': room.member_id,
            'address': room.address,
            'description': room.description,
            'special_notices': room.special_notices,
            'bed_type_id': room.bed_type_id,
            'room_type_id': room.room_type_id,
            'property_type_id': room.property_type_id,
            'max_guess': room.max_guess,
            'num_bathrooms': room.num_bathrooms,
            'num_bedrooms': room.num_bedrooms,
            'num_beds': room.num_beds,
            'status': room.status,
            'apartment_manual': room.apartment_manual,
            'apartment_rule': room.apartment_rule,
            'created_at': room.created_at
        }
    return jsonify(res)
