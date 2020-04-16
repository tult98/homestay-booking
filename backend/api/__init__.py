from homestay import api

from api.resources.user import ns as user_ns
from api.resources.user_profile import ns as user_profile_ns
from api.resources.auth import ns as auth_ns
from api.resources.promotion import ns as promotion_ns
from api.resources.member import ns as member_ns
from api.resources.member_profile import ns as member_profile_ns
from api.resources.booking import ns as booking_ns
from api.resources.image import ns as image_ns
from api.resources.like import ns as like_ns
from api.resources.accommodation import ns as accommodation_ns
from api.resources.comment import ns as comment_ns

api.add_namespace(user_ns)
api.add_namespace(user_profile_ns)
api.add_namespace(auth_ns)
api.add_namespace(promotion_ns)
api.add_namespace(member_ns)
api.add_namespace(member_profile_ns)
api.add_namespace(booking_ns)
api.add_namespace(image_ns)
api.add_namespace(like_ns)
api.add_namespace(accommodation_ns)
api.add_namespace(comment_ns)