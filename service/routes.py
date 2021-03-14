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
from flask import Flask, jsonify, request, url_for, make_response, abort
from flask_api import status  # HTTP Status Codes

# For this example we'll use SQLAlchemy, a popular ORM that supports a
# variety of backends including SQLite, MySQL, and PostgreSQL
from flask_sqlalchemy import SQLAlchemy
from service.models import Promotions, DataValidationError

# Import Flask application
from . import app

######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """ Root URL response """
    return (
        "Reminder: return some useful information in json format about the service here",
        status.HTTP_200_OK,
    )

######################################################################
# CREATE PROMOTION
######################################################################
@app.route("/promotions", methods=["POST"])
def create_promotions():
    """Creates a Promotion"""

######################################################################
# DELETE PROMOTION
######################################################################
@app.route("/promotions/<int:promotion_id>", methods=["DELETE"])
def delete_promotion(promotion_id):
    """Delete a Promotion"""

######################################################################
# LIST ALL PROMOTIONS
######################################################################
@app.route("/promotions", methods=["GET"])
def list_promotions():
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
    return make_response(jsonify(results), status.HTTP_200_OK)


######################################################################
# GET PROMOTION
######################################################################
@app.route("/promotions/<int:promotion_id>", methods=["GET"])
def get_promotion(promotion_id):
    """Get promotion"""

######################################################################
# UPDATE PROMOTION
######################################################################
@app.route("/promotions/<int:promotion_id>", methods=["PUT"])
def update_promotion(promotion_id):
    """Update a promotion"""

######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################

def init_db():
    """ Initialies the SQLAlchemy app """
    global app
    Promotions.init_db(app)


def check_content_type(media_type):
    """ Checks that the media type is correct """
    content_type = request.headers.get("Content-Type")
    if content_type and content_type == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(415, "Content-Type must be {}".format(media_type))