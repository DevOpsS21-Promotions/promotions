"""
Promotions
RESTful service for Promotions

GET /promotions - Returns a list all of the Promotions
GET /promotions/{id} - Returns the Promotion with a given id number
POST /promotions - creates a new Promotion record in the database
PUT /promotions/{id} - updates a Promotion record in the database
DELETE /promotions/{id} - deletes a Promotion record in the database

"""



import os
import sys
import logging
from flask import Flask, jsonify, request, url_for, make_response, abort, render_template
from flask_api import status  # HTTP Status Codes
from flask_restx import Api, Resource, fields, reqparse, inputs

# For this example we'll use SQLAlchemy, a popular ORM that supports a
# variety of backends including SQLite, MySQL, and PostgreSQL
from flask_sqlalchemy import SQLAlchemy
from service.models import Promotions, DataValidationError

# Import Flask application
from . import app

#Import DateTime
import datetime

from werkzeug.exceptions import NotFound

######################################################################
# Configure the Root route before OpenAPI
######################################################################
@app.route('/')
def index():
    """ Index page """
    #return render_template('index.html')
    return app.send_static_file('index.html')

######################################################################
# Configure Swagger before initializing it
######################################################################
api = Api(app,
          version='1.0.0',
          title='Promotion REST API Service',
          description='This the promotion service',
          default='promotions',
          default_label='Promotions operations',
          doc='/apidocs' # default also could use doc='/apidocs/'
         )


# Define the model so that the docs reflect what can be sent
create_model = api.model('Promotion', {
    'name': fields.String(required=True,
                          description='The name of the Promotion'),
    'description': fields.String(required=True,
                              description='The description of the Promotion'),
    'promo_code': fields.String(required=True,
                              description='The promo code of the Promotion'),
    'start_date': fields.DateTime(required=True,
                              description='The start date and time of the Promotion'),    
    'end_date': fields.DateTime(required=True,
                              description='The end date and time of the Promotion'),                        
    'is_active': fields.Boolean(required=True,
                                description='Is the Promotion active')
})

promotion_model = api.model(
    'Promotion', 
    {
        'id': fields.Integer(readOnly=True,
                            description='The unique id assigned internally by service'),
        'name': fields.String(required=True,
                            description='The name of the Promotion'),
        'description': fields.String(required=True,
                                description='The description of the Promotion'),
        'promo_code': fields.String(required=True,
                                description='The promo code of the Promotion'),
        'start_date': fields.DateTime(required=True,
                                description='The start date and time of the Promotion'),    
        'end_date': fields.DateTime(required=True,
                                description='The end date and time of the Promotion'),                        
        'is_active': fields.Boolean(required=True,
                                    description='Is the Promotion active')
    }
)

# query string arguments
promotion_args = reqparse.RequestParser()
promotion_args.add_argument('name', type=str, required=False, help='List Promotions by name')

######################################################################
# Error Handlers
######################################################################
@app.errorhandler(DataValidationError)
def request_validation_error(error):
    """ Handles Value Errors from bad data """
    return bad_request(error)

@app.errorhandler(status.HTTP_400_BAD_REQUEST)
def bad_request(error):
    """ Handles bad reuests with 400_BAD_REQUEST """
    app.logger.warning(str(error))
    return (
        jsonify(
            status=status.HTTP_400_BAD_REQUEST, error="Bad Request", message=str(error)
        ),
        status.HTTP_400_BAD_REQUEST,
    )


@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    """ Handles resources not found with 404_NOT_FOUND """
    app.logger.warning(str(error))
    return (
        jsonify(
            status=status.HTTP_404_NOT_FOUND, error="Not Found", message=str(error)
        ),
        status.HTTP_404_NOT_FOUND,
    )


@app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)
def method_not_supported(error):
    """ Handles unsuppoted HTTP methods with 405_METHOD_NOT_SUPPORTED """
    app.logger.warning(str(error))
    return (
        jsonify(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            error="Method not Allowed",
            message=str(error),
        ),
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )


@app.errorhandler(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
def mediatype_not_supported(error):
    """ Handles unsuppoted media requests with 415_UNSUPPORTED_MEDIA_TYPE """
    app.logger.warning(str(error))
    return (
        jsonify(
            status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            error="Unsupported media type",
            message=str(error),
        ),
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    )


@app.errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    """ Handles unexpected server error with 500_SERVER_ERROR """
    app.logger.error(str(error))
    return (
        jsonify(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error="Internal Server Error",
            message=str(error),
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

######################################################################
#  PATH: /promotions/{id}
######################################################################
@api.route('/promotions/<promotion_id>')
@api.param('promotion_id', 'The Promotion identifier')
class PromotionResource(Resource):
    """
    PromotionResource class
    Allows the manipulation of a single Promotion
    GET /promotion/{id} - Returns a Promotion with the id
    PUT /promotion/{id} - Update a Promotion with the id
    DELETE /promotion/{id} -  Deletes a Promotion with the id
    """

    ######################################################################
    # GET PROMOTION
    ######################################################################
    @api.doc('get_promotions')
    @api.response(404, 'Promotion not found')
    @api.marshal_with(promotion_model)
    def get(self, promotion_id):
        """Get promotion"""

        app.logger.info("Request for Promotion with id: %s", promotion_id)
        promotion = Promotions.find(promotion_id)
        if not promotion:
            api.abort(status.HTTP_404_NOT_FOUND, "Promotion with id '{}' was not found.".format(promotion_id))
        app.logger.info("Returning Promotion: %s", promotion.name)
        return promotion.serialize(), status.HTTP_200_OK

    ######################################################################
    # UPDATE PROMOTION
    ######################################################################
    @api.doc('update_promotions')
    @api.response(404, 'Promotion not found')
    @api.response(400, 'The posted Promotion data was not valid')
    @api.expect(promotion_model)
    @api.marshal_with(promotion_model)
    def put(self, promotion_id):
        """Update a promotion"""

        app.logger.info("Request to update promotion with id: %s", promotion_id)
        check_content_type("application/json")
        promotion = Promotions.find(promotion_id)
        if not promotion:
            api.abort(status.HTTP_404_NOT_FOUND, "Promotion with id '{}' was not found.".format(promotion_id))
        promotion.deserialize(request.get_json())
        promotion.id = promotion_id
        promotion.update()
        app.logger.info("Promotion with ID [%s] updated.", promotion.id)
        return promotion.serialize(), status.HTTP_200_OK

    ######################################################################
    # DELETE PROMOTION
    ######################################################################
    @api.doc('delete_promotions')
    @api.response(204, 'Promotion deleted')
    def delete(self, promotion_id):
        app.logger.info("Request to delete promotion with id: %s", promotion_id)
        promotion = Promotions.find(promotion_id)
        if promotion:
            promotion.delete()
        app.logger.info("Promotion with ID [%s] delete complete.", promotion_id)
        return '', status.HTTP_204_NO_CONTENT

######################################################################
#  PATH: /promotions
######################################################################
@app.route("/promotions", strict_slashes=False)
class PromotionCollection(Resource):
    """ Handles all interactions with collections of Promotions """

    ######################################################################
    # CREATE PROMOTION
    ######################################################################
    @api.doc('create_promotion')
    @api.expect(create_model)
    @api.response(400, 'The posted data was not valid')
    @api.response(201, 'Promotion created successfully')
    @api.marshal_with(promotion_model, code=201)
    def post(self):
        """Creates a Promotion"""
        app.logger.info("Request to create a promotion")
        check_content_type("application/json")
        promotion = Promotions()
        try:
            promotion.deserialize(request.get_json())
        except DataValidationError as dataValidationError:
            api.abort(status.HTTP_400_BAD_REQUEST, dataValidationError)
        promotion.create()
        location_url = api.url_for(PromotionResource, promotion_id=promotion.id, _external=True)
        app.logger.info("Promotion with ID [%s] created.", promotion.id)
        return promotion.serialize(), status.HTTP_201_CREATED, {'Location': location_url}

    ######################################################################
    # LIST ALL PROMOTIONS
    ######################################################################
    @api.doc('list_promotions')
    @api.expect(promotion_args, validate=True)
    @api.marshal_list_with(promotion_model)
    def get(self):
        """ 
        Get all Promotions 
        This endpoint will list all promotions based on the data that is stored
        """
        app.logger.info("Request for promotions list")
        promotion = []
        name = request.args.get("name")
        if name:
            promotion = Promotions.find_by_name(name)
        else:
            promotion = Promotions.all()

        results = [promotion.serialize() for promotion in promotion]
        app.logger.info("Returning %d promotions", len(results))
        return results, status.HTTP_200_OK

######################################################################
#  PATH: /promotions/{id}/cancel
######################################################################
@api.route('/promotions/<promotion_id>/cancel')
@api.param('promotion_id', 'The Promotion identifier')
class CancelResource(Resource):

    ######################################################################
    # CANCEL PROMOTION
    ######################################################################
    @api.doc('purchase_promotions')
    @api.response(404, 'Promotion not found')
    @api.response(409, 'The Promotion is not available for purchase')
    def put(self, promotion_id):
        """Cancel a promotion"""

        app.logger.info("Request to cancel promotion with id: %s", promotion_id)
        promotion = Promotions.find(promotion_id)
        if not promotion:
            api.abort(status.HTTP_404_NOT_FOUND, 'Promotion with id [{}] was not found.'.format(promotion_id))
        promotion.end_date = datetime.datetime.now()
        promotion.is_active = False
        promotion.id = promotion_id
        promotion.update()
        app.logger.info("Promotion with ID [%s] canceled.", promotion.id)
        return promotion.serialize(), status.HTTP_200_OK

######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################

@app.before_first_request
def init_db():
    """ Initialies the SQLAlchemy app """
    global app
    Promotions.init_db(app)

def check_content_type(content_type):
    """ Checks that the media type is correct """
    if request.headers["Content-Type"] == content_type:
        return
    app.logger.error("Invalid Content-Type: %s", request.headers["Content-Type"])
    abort(415, "Content-Type must be {}".format(content_type))