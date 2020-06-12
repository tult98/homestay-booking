import json
from homestay.models.models import RoomType, BedType, Amenity_category, Amenity, Accommodation, Image, PropertyType, \
    Member, AccommodationAmenity
from homestay import db


def convert_time(time_string):
    return datetime.strptime(time_string,'%H:%M %p')



def read_json(file_output_path):
    with open('json/' + file_output_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_db(name_db):
    db.session.add(name_db)
    db.session.commit()


def insert_room_types():
    data = read_json('room_types.json')
    for i in data:
        room_types = RoomType(id=i['id'], name=i['name'])
        save_db(room_types)


def insert_bed_types():
    data = read_json('bed_types.json')
    for i in data:
        bed_types = BedType(id=i['id'], name=i['name'])
        save_db(bed_types)


def insert_amenity_types():
    data = read_json('amenity_types.json')
    for i in data:
        amenity_category = Amenity_category(id=i['id'], name=i['name'])
        save_db(amenity_category)


def insert_amenities():
    data = read_json('amenities.json')
    for i in data:
        amenity = Amenity(id=i['id'], amenity_category_id=i['amenity_types_id'], name=i['name'])
        save_db(amenity)


def insert_member():
    data = read_json('member.json')
    for i in data:
        member = Member(_id=i['id'], email=i['username'], hash_password=i['hash_password'], role=i['role'])
        save_db(member)


def insert_property_type():
    data = read_json('property_types.json')
    for i in data:
        property_type = PropertyType(id=i['id'], name=i['name'])
        save_db(property_type)


def insert_room():
    data = read_json('rooms.json')
    for i in data:
        if i['property_type'] == "":
            property_type = 1
        else:
            property_type = i['property_type']
        if i['room_type'] == "":
            room_type = 1
        else:
            room_type = i['room_type']
        if i['bed_type'] == "":
            bed_type = 1
        else:
            bed_type = i['bed_type']
        rooms = Accommodation(id=i['id'], member_id=i['member_id'], property_type_id=property_type,
                              room_type_id=room_type, bed_type_id=bed_type, name=i['name'],
                              address=i['address'], description=i['description'], special_notices=i['special_note'],
                              max_guess=i['maximum_guests'], num_bathrooms=i['num_bathrooms'],
                              num_bedrooms=i['num_bedrooms'], num_beds=i['num_beds'],
                              apartment_manual=i['apartment_manual'], apartment_rule=i['apartment_rules'],
                              status=i['status'], checkin_guide="")
        save_db(rooms)


def insert_images():
    data = read_json('images.json')
    for i in data:
        image = Image(id=i['id'], accommodation_id=i['room_id'], image_url=i['photo_url'])
        save_db(image)


def insert_room_amenities():
    data = read_json('room_amenities.json')
    for i in data:
        room_amenities = AccommodationAmenity(accommodation_id=i['room_id'], amenity_id=i['amenities'])
        save_db(room_amenities)


def insert_price():
    data = read_json('prices.json')
    for i in data:
        price = Price(id=i['room_id'], additional_guess_fee=i['additional_guests_fee'], cleaning_fee=i['cleaning_fee'],
                      security_fee=i['security_fee'], monthly_price=i['monthly_price'],
                      nightly_price=i['nightly_price'], weekend_price=i['weekend_price'],
                      cancelation_policy=i['cancellation_policy'], check_in=conert_time(i['checkin_time']),
                      check_out=convert_time(i['checkout_time']))
        save_db(price)
