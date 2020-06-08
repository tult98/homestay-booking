from datetime import datetime
from homestay import db, ma
import random
import string
from sqlalchemy import (and_, or_)

#pylint:disable=E1101
# addition field email on User table
class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    user_profile = db.relationship(
        'UserProfile', backref='user', uselist=False, lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    bookings = db.relationship('Booking', backref='user', lazy=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    role = db.Column(db.Integer, nullable=False)
    hash_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    def __init__(self, _id, email, hash_password, role=1):
        self.id = _id
        self.email = email
        self.hash_password = hash_password
        self.role = role

    def __str__(self): 
        return str({
            "email": self.email,
            "role": self.role
        })

    @property
    def serializer(self): 
        return {
            'id': self.id,
            'email': self.email,
            'role': self.role
        }

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_all_users(cls):
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("email", "role")

    def __init__(self, email, role):
        self.email = email
        self.role = role


# delete field email in UserProfile table
class UserProfile(db.Model):
    user_id = db.Column(db.String(32), db.ForeignKey(
        'user.id'), primary_key=True)
    last_name = db.Column(db.String(255), default=None)
    first_name = db.Column(db.String(255), default=None)
    phone_number = db.Column(db.String(255), default=None)
    gender = db.Column(db.String(255), default=None)
    avatar_url = db.Column(db.String(255), default=None)
    address = db.Column(db.String(255), default=None)
    description = db.Column(db.Text, default=None)
    birthday = db.Column(db.DateTime, default=None)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    def __init__(self, user_id, first_name, last_name, phone_number):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
    
    @classmethod
    def find_by_email(cls, email):
        return db.session.query(UserProfile).join(User).filter(
            User.id == UserProfile.user_id).filter(User.email == email).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(user_id=_id).first()
    
    @classmethod
    def get_all_profile(cls):
        return UserProfile.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class UserProfileSchema(ma.Schema):
    class Meta:
        model = UserProfile
        fields = ("user_id", "first_name", "last_name", "phone_number", "updated_at")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey(
        'user.id'), nullable=False)
    accommodation_id = db.Column(db.String(32), db.ForeignKey(
        'accommodation.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey(
        'user.id'), nullable=False)
    accommodation_id = db.Column(
        db.String(32), db.ForeignKey('accommodation.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)


class RoomType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodations = db.relationship(
        'Accommodation', cascade="all, delete", backref='room_type', lazy=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)


class PropertyType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodations = db.relationship(
        'Accommodation', cascade="all, delete", backref='property_type', lazy=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

class BedType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    accommodations = db.relationship("Accommodation", cascade="all, delete", backref="bed_type", lazy=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

class Accommodation(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    likes = db.relationship('Like', backref='accommodation', lazy=True)
    promotions = db.relationship(
        'Promotion', backref='accommodation', lazy=True)
    comments = db.relationship('Comment', backref='accommodation', lazy=True)
    images = db.relationship('Image', backref='accommodation', lazy=True)
    bookings = db.relationship(
        'Booking', backref='accommodation', lazy=True)
    amenities = db.relationship(
        'Amenity', secondary='link')
    member_id = db.Column(db.String(32), db.ForeignKey('member.id'),nullable=False)
    property_type_id = db.Column(
        db.Integer, db.ForeignKey('property_type.id'), nullable=False)
    room_type_id = db.Column(db.Integer, db.ForeignKey('room_type.id'), nullable=False)
    bed_type_id = db.Column(db.Integer, db.ForeignKey('bed_type.id'))
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(255))
    description = db.Column(db.Text)
    special_notices = db.Column(db.Text)
    status = db.Column(db.String, nullable=False)
    max_guess = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.SmallInteger)
    num_bedrooms = db.Column(db.SmallInteger)
    num_beds = db.Column(db.SmallInteger)
    apartment_manual = db.Column(db.Text)
    apartment_rule = db.Column(db.Text)
    direction_manual = db.Column(db.Text)
    checkin_guide = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def get_all_accommodation(cls):
        return cls.query.all()

    @classmethod
    def filter_accommodatons(cls, data):

        query = db.session.query(Accommodation).join(PropertyType).join(BedType).join(RoomType)

        if data.property_type != None:
            query = query.filter(PropertyType.name==data.property_type)
        
        if data.price != None: 
            query = query.filter(Accommodation.price==data.price)
        
        if data.room_type != None: 
            query = query.filter(RoomType.name==data.room_type)
        
        if data.bed_type != None:
            query = query.filter(BedType.name==data.bed_type)
        
        if data.max_guess != None:
            query = query.filter(Accommodation.max_guess==data.max_guess)
        
        if data.num_beds != None:
            query = query.filter(Accommodation.num_beds==data.num_beds)
        
        if data.num_bathrooms != None:
            query = query.filter(Accommodation.num_bathrooms==data.num_bathrooms)

        if data.num_bedrooms != None:
            query = query.filter(Accommodation.num_bedrooms==data.num_bedrooms)

        return query
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodation_id = db.Column(
        db.String(32), db.ForeignKey('accommodation.id'))
    member_id = db.Column(
        db.String(32), db.ForeignKey('member.id'))
    image_url = db.Column(db.String(255), default=None)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def get_all_image(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod 
    def find_by_url(cls, url):
        return cls.query.filter_by(image_url=url).first()
    
    @classmethod
    def get_image_by_accommodation_id(cls, accommodation_id):
        return db.session.query(Image).join(Accommodation).filter(
            Image.accommodation_id == Accommodation.id).filter(Accommodation.id == accommodation_id).all()
    
    def delete(self):
        db.session.delete(self)
        db.commit()

    def save_to_db(self):
        db.session.add(self)
        db.commit()


class ImageSchema(ma.Schema):
    class Meta:
        model = Image
        fields = ("id", "accommodation_id", "image_url")

# modify field username to email in Member table 
class Member(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    accommodations = db.relationship(
        'Accommodation', cascade="all, delete", backref='member', lazy=True)
    promotions = db.relationship('Promotion', backref='member', lazy=True)
    images = db.relationship('Image', backref='member', lazy=True)
    bookings = db.relationship('Booking', backref='member', lazy=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hash_password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    def __init__(self, _id, email, hash_password, role=0):
        self.email = email
        self.hash_password = hash_password
        self.role = role
        self.id = _id

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_all_member(cls):
        return cls.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class MemberSchema(ma.Schema):
    class Meta:
        model = Member
        fields = ("id", "email", "role")


# delete field email in MemberProfile table 
class MemberProfile(db.Model):
    member_id = db.Column(db.String(32), db.ForeignKey(
        'member.id'), primary_key=True)
    name = db.Column(db.String(255), default=None)
    phone_number = db.Column(db.String(255), default=None)
    gender = db.Column(db.String(255), default=None)
    avatar_url = db.Column(db.String(255), default=None)
    address = db.Column(db.String(255), default=None)
    identify_documentID = db.Column(db.String(255), default=None)
    identify_document_url = db.Column(db.String(255), default=None)
    description = db.Column(db.Text, default=None)
    birthday = db.Column(db.DateTime, default=None)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    def __init__(self, member_id, name, phone_number):
        self.member_id = member_id
        self.name = name
        self.phone_number = phone_number
    
    @classmethod
    def find_by_email(cls, email):
        return db.session.query(MemberProfile).join(Member).filter(
            Member.id == MemberProfile.member_id).filter(Member.email == email).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(member_id=_id).first()
    
    @classmethod
    def get_all_profile(cls):
        return cls.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class MemberProfileSchema(ma.Schema):
    class Meta:
        model = MemberProfile
        fields = ("member_id", "name", "phone_number")


class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amenity_category_id = db.Column(
        db.Integer, db.ForeignKey('amenity_category.id'))
    accommodations = db.relationship(
        'Accommodation', secondary='link')
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)


class Amenity_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amenities = db.relationship(
        'Amenity', backref='amenity_category', lazy=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey('user.id'))
    member_id = db.Column(db.String(32), db.ForeignKey('member.id'))
    accommodation_id = db.Column(
        db.String(32), db.ForeignKey('accommodation.id'))
    code = db.Column(db.String(255), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False, default=0)
    number_of_guess = db.Column(db.Integer, nullable=False)
    number_of_night = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    check_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    check_out = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)
    
    @classmethod
    def code_generation(cls):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(6))

    @classmethod
    def get_all_booking(cls):
        return cls.query.all()

    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code=code).first()

    @classmethod
    def get_booking_by_user_id(cls, user_id):
        return db.session.query(Booking).join(User).filter(
            Booking.user_id == User.id).filter(User.id == user_id).all()
    
    @classmethod
    def get_booking_by_member_id(cls, member_id):
        return db.session.query(Booking).join(Member).filter(
            Booking.member_id == Member.id).filter(Member.id == member_id).all()
    
    @classmethod
    def get_booking_by_accommodation_id(cls, accommodation_id):
        return db.session.query(Booking).join(Accommodation).filter(
            Booking.accommodation_id == Accommodation.id).filter(Accommodation.id == accommodation_id).first()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class BookingSchema(ma.Schema):
    class Meta:
        model = Booking
        fields = ("id", "code", "status", "number_of_guess", "number_of_night",
                  "total_price", "check_in", "check_out", "created_at", "updated_at")


class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodation_id = db.Column(
        db.String(32), db.ForeignKey('accommodation.id'))
    member_id = db.Column(db.String(32), db.ForeignKey('member.id'))
    code = db.Column(db.String(255), nullable=False)
    discount_amount = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)

    
    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code=code).first()
    
    @classmethod
    def get_all_promotion(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_promotion_by_member_id(cls, id):
        return db.session.query(Promotion).join(Member).filter(
            Promotion.member_id == Member.id).filter(Member.id == id).all()

    @classmethod 
    def get_promotion_by_accommodation_id(cls, id):
        return db.session.query(Promotion).join(Accommodation).filter(
            Promotion.accommodation_id == Accommodation.id).filter(Accommodation.id == id).all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class AccommodationAmenity(db.Model):
    __tablename__ = 'link'
    accommodation_id = db.Column(db.String(32), db.ForeignKey(
        'accommodation.id'), primary_key=True)
    amenity_id = db.Column(db.Integer, db.ForeignKey(
        'amenity.id'), primary_key=True)

# class Price(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     additional_guess_fee = db.Column(db.Float, nullable=False, default=0)
#     cleaning_fee = db.Column(db.Float, nullable=False, default=0)
#     security_fee = db.Column(db.Float, nullable=False, default=0)
#     monthly_price = db.Column(db.Float, nullable=False)
#     nightly_price = db.Column(db.Float, nullable=False)
#     weekend_price = db.Column(db.Float, nullable=False)
#     cancelation_policy = db.Column(db.Text)
#     check_in = db.Column(db.DateTime, nullable=False)
#     check_out = db.Column(db.DateTime, nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False,
#                            default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False,
#                            default=datetime.utcnow)
#     deleted_at = db.Column(db.DateTime)


class RevokedTokenModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def __init__(self, jti):
        self.jti = jti

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
