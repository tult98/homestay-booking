from flask_restplus import fields 
from homestay import api

promotion = api.model("Promotion", {
    "id": fields.Integer(description="Id of promotion"),
    'code': fields.String(required=True, description="Code of promotion"),
    'discount_amount': fields.Float(required=True, description="The amount of discount"),
    'start_time': fields.DateTime(required=True, description="The time when guess arrived homestay", 
                                    example="2019-07-23 07:53:03"),
    'end_time': fields.DateTime(required=True, description="The time when guess leave homestay",
                                  example="2019-07-23 07:53:03")
})

user_register = api.model("User1", {
    'email': fields.String(required=True, description="email of user account"),
    'first_name': fields.String(required=True, description="firtname of user"),
    'last_name': fields.String(required=True, description="lastname of user"),
    'phone_number': fields.String(required=True, description="Phone number of user"),
    'password1': fields.String(required=True, description="The password for account"),
    "password2": fields.String(required=True, description="Confirm password")
})

user_login = api.model("User2", {
    'email': fields.String(required=True, description="Email of user"),
    'password': fields.String(required=True, description="Password of user account")
})

user = api.model("User3", {
    'id': fields.String(description="uuid of user account"),
    'email': fields.String(required=True, description="email of user account"),
    'hash_password': fields.String(required=True, description="The password for account"),
    "role": fields.Integer(required=True, description="Role of member")
})

user_profile = api.model("UserProfile", {
    'user_id': fields.String(description="uuid of user account"),
    'email': fields.String(required=True, description="email of user account"),
    'first_name': fields.String(required=True, description="The firstname of user"),
    'last_name': fields.String(required=True, description="The lastname of user"),
    'phone_number': fields.String(required=True, description="The phone number of user"),
    "gender": fields.String(description="Gender of user"),
    'address': fields.String(description="address of user"),
    'birthday': fields.DateTime(description="Birthday of user"),
    'avatar_url': fields.String(description="avatar_url of user"),
})

token = api.model("UserProfile", {
    'token': fields.String(description="token for account", example="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjM4NjY5MTQsIm5iZiI6MTU2Mzg2NjkxNCwianRpIjoiMDUxNjE3NTQtNmQ3OC00NzE4LTgyYWMtYTNjMWNhY2JkYTU3IiwiZXhwIjoxNTY2NDU4OTE0LCJpZGVudGl0eSI6IjJkNDdlYTM1OGFiMzRjODNiOWYyOGU4ZTM1ZDY4ZTQ2IiwidHlwZSI6InJlZnJlc2gifQ.ExvdQbj-l496F0YVDlnpo1tBdlAfMAU0BnxoS7rCRP0")
})

member_register = api.model("Member1", {
    'email': fields.String(required=True, description="email of member account"),
    'name': fields.String(required=True, description="Name of member"),
    'phone_number': fields.String(required=True, description="Phone number of member"),
    'password1': fields.String(required=True, description="The password for account"),
    "password2": fields.String(required=True, description="Confirm password"),
    # "role": fields.Integer(required=True, description="Role of member")
})

member = api.model("Member2", {
    'id': fields.String(description="uuid of member account"),
    'email': fields.String(required=True, description="email of member account"),
    'hash_password': fields.String(required=True, description="The password for account"),
    "role": fields.Integer(required=True, description="Role of member")
})

member_login = api.model("Member3", {
    'email': fields.String(required=True, description="Code of promotion"),
    'password': fields.String(required=True, description="Password of user account")
})

member_profile = api.model("MemberProfile", {
    'member_id': fields.String(description="uuid of member account"),
    'email': fields.String(required=True, description="email of member account"),
    'name': fields.String(required=True, description="The name of member"),
    'phone_number': fields.String(required=True, description="The phone number of member"),
    "identify_documentID": fields.String(required=True, description="The identify number ID of member"),
    "identify_document_url": fields.String(required=True, description="The identify_url of member"),
    "gender": fields.String(description="Gender of member"),
    'address': fields.String(description="address of member"),
    'birthday': fields.DateTime(description="Birthday of member"),
    'avatar_url': fields.String(description="avatar_url of member"),
})

booking_create = api.model("Booking1", {
    'status': fields.Integer(required=True, description="status of booking", default="0"),
    'number_of_guess': fields.Integer(required=True, description="The number of guess arrived"),
    'number_of_night': fields.Integer(required=True, description="The number of night guess will stay"),
    'total_price': fields.Float(required=True, description="Total price of booking"),
    'check_in': fields.DateTime(required=True, description="check_in time of guess", example="2019-07-23 07:53:03"),
    'check_out': fields.DateTime(required=True, description="check_out time of guess", example="2019-07-23 07:53:03")
})

booking = api.model("Booking2", {
    'code': fields.String(description="code of booking"),
    'status': fields.String(required=True, description="status of booking"),
    'number_of_guess': fields.String(required=True, description="The number of guess arrived"),
    'number_of_night': fields.String(required=True, description="The number of night guess will stay"),
    'total_price': fields.String(required=True, description="Total price of booking")
})

image = api.model("Image", {
    "id": fields.Integer(description="id of image"),
    "member_id": fields.String(required=True, description="Id of member who upload this image"),
    "accommodation_id": fields.String(required=True, description="id of accommodation that image belong to"),
    "image_url": fields.String(required=True, description="url of image"),
    "created_at": fields.DateTime(description="The time when create image")
})

like = api.model("Like", {
    "user_id": fields.String(required=True, description="id of user create this like"),
    "accommodation_id": fields.String(required=True, description="id of accommodation this user like"),
    "created_at": fields.DateTime(description="The time when this user like accommodation")
})

room_type = api.model("RoomType", {
    "name": fields.String(required=True, description="Name of room type")
})

bed_type = api.model("RoomType", {
    "name": fields.String(required=True, description="Name of bed type")
})

property_type = api.model("RoomType", {
    "name": fields.String(required=True, description="Name of property type")
})

accommodation_create = api.model("Accommodation1", {
    "name": fields.String(required=True, description="name of accommodation"),
    "property_type_id": fields.Integer(required=True, desceiprion="type of  accommodation"),
    "room_type_id": fields.Integer(required=True, desceiption="room type of accommodation"),
    "bed_type_id": fields.Integer(required=True, description="bed type of accmmodation"),
    "standard_guess": fields.Integer(required=True, description="standard number of guess"),
    "max_guess": fields.Integer(required=True, description="Maximum number of guess"),
    "status": fields.Integer(required=True, description="status of accmmodation", default="0"),
})

accommodation_search = api.model("Accommodation3", {
    "property_type": fields.String(description="name of accommodation"),
    "bed_type": fields.String(desceiprion="type of  accommodation"),
    "room_type": fields.String(desceiption="room type of accommodation"),
    "max_guess": fields.Integer(description="number of guest of accommodation"),
    "num_beds": fields.Integer(description="number of bed of accommodation"),
    "num_bedrooms": fields.Integer(description="number of bed room number of accommodation"),
    "num_bathrooms": fields.Integer(description="number of bathroom of accommodation"),
    # "price": fields.Float(description="Price of accommodation")
})

accommodation = api.model("Accommodation2", {
    "id": fields.String(required=True, description="id of accommodation"),
    "name": fields.String(required=True, description="name of accommodation"),
    "member_id": fields.String(required=True, description="id of member who own this accommodation"),
    # "property_type_id": fields.Integer(required=True, desceiprion="type of  accommodation"),
    'property_type': fields.Nested(property_type),
    'room_type': fields.Nested(room_type),
    'bed_type': fields.Nested(bed_type),
    'images': fields.Nested(image, skip_none=True),
    # "room_type_id": fields.Integer(required=True, desceiption="room type of accommodation"),
    "standard_guess": fields.Integer(required=True, description="standard number of guess"),
    "max_guess": fields.Integer(required=True, description="Maximum number of guess"),
    "status": fields.String(required=True, description="status of accmmodation", default="Waiting"),
    "address": fields.String(description="address of accommodation"),
    "num_bathrooms": fields.Integer(description="Number of bathroom"),
    "num_beds": fields.Integer(description="Number of bed"),
    # "bed_type_id": fields.String(desceiption="type of bed in accommodation"),
    "description": fields.String(description="description of accommodation"),
    "special_notices": fields.String(description="special_notices of accommodation"),
    "num_bedrooms": fields.Integer(description="Number of bedroom"),
    "apartment_manual": fields.String(description="apartment_manual of accommodation"),
    "apartment_rule": fields.String(description="apartment_manual of accommodation"),
    "direction_manual": fields.String(description="direction_manual of accommodation"),
    "checkin_guide": fields.String(description="checkin_guide of accommodation"),
})

comment = api.model("Comment", {
    "user_id": fields.String(required=True, description="id of user who created that comment"),
    "accommodation_id": fields.String(required=True, description="id of accommodation "),
    "content": fields.String(required=True, desceiprion="content of  comment")
})
