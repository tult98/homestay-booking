from flask import make_response, jsonify, abort, request
from homestay import app
from homestay.models.models import Price
from homestay import db


@app.route('/api/price', methods=['GET'])
def price():
    if request.method == 'GET':
        response_object = []
        prices = Price.query.all()
        if not prices:
            return jsonify({'mess': 'price is None'})
        else:
            for i in prices:
                response_object.append({
                    'id': i.accommodation_id,
                    'additional_guess_fee': i.additional_guess_fee,
                    'cleaning_fee': i.cleaning_fee,
                    'security_fee': i.security_fee,
                    'monthly_price': i.monthly_price,
                    'nightly_price': i.nightly_price,
                    'weekend_price': i.weekend_price,
                    'cancelation_policy': i.cancelation_policy,
                    'check_in': i.check_in,
                    'check_out': i.check_out
                })
            return make_response(jsonify(response_object)), 200


@app.route('/api/price/<int:id>', methods=['GET', 'PUT'])
def price_id(id):
    if request.method == 'GET':
        price = Price.query.filter_by(id=id).first_or_404()
        if not price:
            return jsonify({'mess': 'price is None'})
        res = {
            'id': price.accommodation_id,
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
    if request.method == 'PUT':
        price = Price.query.filter_by(id=id).first_or_404()
        data = request.get_json()
        for i in data:
            setattr(price, i, data[i])
        db.session.add(price)
        db.session.commit()
        res = {
            'id': price.accommodation_id,
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
