from flask_restful import Resource, reqparse
from homestay.models.models import Image, Accommodation
from homestay import api
from api import serializers
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_claims,
    get_jwt_identity
)

ns = api.namespace('api/image', description="Operations related to image")

@ns.route('/<string:accommodation_id>')
class ImageAccommodationListAPI(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'accommodation_id': 'The id of accommodation that we want to get images'})
    # @jwt_required
    def get(self, accommodation_id):
        """
        Return the list of image that accommodation have\n
        <h2>Implementation Notes:</h2>
        <p>Use this method to get the list of image belong to specify accommodation</p>
        <ul>
            <li>Specify by id of accommodation that you want to get list of image in URL path</li>
        </ul>
        """
        accommodation = Accommodation.find_by_id(accommodation_id)
        if not accommodation:
            api.abort(code=404, message="Cannot find the accmmodation you need")
        member_id = accommodation.member_id
        current_id = get_jwt_identity()
        role = get_jwt_claims()['role']
        if not (role == 3 or current_id == member_id):
            api.abort(code=400, message="You dont have permission")
        images = accommodation.images
        if len(images) == 0:
            return {"message": "This accommodation doesnt have any image yet"}, 200
        return images, 200
        
@ns.route('/create')
class ImageCreateAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("accommodation_id", type=str,required=True)
    parser.add_argument("image_url", type=str,required=True)

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(serializers.image)
    def post(self):
        """
        Create a image\n
            <h2>Implementation Notes:</h2>
            <p>Use this method to create a new image</p>
            <ul>
                <li>Send a JSON object with the id of accommodation, member, image_url in the request body</li>
            </ul>
        """
        data = self.parser.parse_args()
        accommodation = Accommodation.find_by_id(data['accommodation_id'])
        if not accommodation:
            api.abort(code=404, message="Cannot find the accommodation you need")
        member_id = accommodation.member_id
        current_id = get_jwt_identity()
        role = get_jwt_claims()['role']
        if not (role == 3 or current_id == member_id):
            api.abort(code=400, message="You dont have permisson")
        if Image.find_by_url(data['image_url']):
            return {
                "message": "This image already exist"
            }, 400
        image = Image(member_id=current_id, accommodation_id=data['accommodation_id'], image_url=data['image_url'])
        image.save_to_db()
        return {
            "message": "Upload image success"
        }, 200

@ns.route('/<image_id>')
class ImageAPI(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'The id of image'})
    @api.marshal_with(serializers.image)
    def get(self, image_id):
        """
        Return detail a image with a given id\n
        <h2>Implementation Note:</h2>\n
        Use this method to get detail of  a image with a given id
        <ul>
            <li>Specify the ID of the image to get in the request URL path</li>
        </ul>
        """
        image = Image.find_by_id(image_id)
        if image:
            return image, 200
        return {
            "success": 0,
            "message": "Cannot find that image"
        }, 400

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'The id of image'})
    # @jwt_required
    def delete(self, image_id):
        """
        Delete a image with a given id\n
        <h2>Implementation Note:</h2>\n
        Use this method to delete a image with a given id
        <ul>
            <li>Specify the ID of the image to get in the request URL path</li>
        </ul>
        """
        role = get_jwt_claims()['role']
        current_id = get_jwt_identity()
        image = Image.find_by_id(image_id)
        if image:
            if not (role==3 or current_id==image.member_id):
                api.abort(code=400, message="You dont have permission")
            image.delete()
            return {
                "message": "Delete image success"
            }, 200
        return {
            "message": "Cannot find the image that you need"
        }, 404

