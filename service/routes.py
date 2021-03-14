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
    app.logger.info("Request to delete pet with id: %s", promotion_id)
    promotion = Promotions.find(promotion_id)
    if promotion:
        promotion.delete()

    app.logger.info("Promotion with ID [%s] delete complete.", promotion_id)
    return make_response("", status.HTTP_204_NO_CONTENT)

######################################################################
# LIST ALL PROMOTIONS
######################################################################
@app.route("/promotions", methods=["GET"])
def list_promotions():
    """ Get all Promotions """

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

