"""
Models for Promotions

All of the models are stored in this module
"""
import logging
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

logger = logging.getLogger("flask.app")

# Create the SQLAlchemy object to be initialized later in init_db()
db = SQLAlchemy()

DATETIME = "%Y-%m-%d %H:%M:%S"

class DataValidationError(Exception):
    """ Used for an data validation errors when deserializing """

    pass


class Promotions(db.Model):
    """
    Class that represents a <your resource model name>
    """

    app = None

    ##################################################
    # Table Schema
    ##################################################
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    description = db.Column(db.String(140))
    promo_code = db.Column(db.Integer())
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    modified_date = db.Column(db.DateTime())
    created_date = db.Column(db.DateTime())
    is_active = db.Column(db.Boolean())

    ##################################################
    # INSTANCE METHODS
    ##################################################

    def __repr__(self):
        return "<Promotions %r id=[%s]>" % (self.name, self.id)

    def create(self):
        """
        Creates a Promotions to the database
        """
        logger.info("Creating %s", self.name)
        self.id = None  # id must be none to generate next primary key
        db.session.add(self)
        db.session.commit()

    def save(self):
        """
        Updates a Promotions to the database
        """
        logger.info("Saving %s", self.name)
        db.session.commit()

    def delete(self):
        """ Removes a Promotions from the data store """
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """ Serializes a Promotions into a dictionary """
        return {"id": self.id, "name": self.name}

    def deserialize(self, data):
        """
        Deserializes a Promotions from a dictionary

        Args:
            data (dict): A dictionary containing the resource data
        """
        try:
            self.name = data["name"]
        except KeyError as error:
            raise DataValidationError(
                "Invalid Promotions: missing " + error.args[0]
            )
        except TypeError as error:
            raise DataValidationError(
                "Invalid Promotions: body of request contained bad or no data"
            )
        return self

    @classmethod
    def init_db(cls, app):
        """ Initializes the database session """
        logger.info("Initializing database")
        cls.app = app
        # This is where we initialize SQLAlchemy from the Flask app
        db.init_app(app)
        app.app_context().push()
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def all(cls):
        """ Returns all of the Promotionss in the database """
        logger.info("Processing all Promotionss")
        return cls.query.all()

    @classmethod
    def find(cls, by_id):
        """ Finds a Promotions by it's ID """
        logger.info("Processing lookup for id %s ...", by_id)
        return cls.query.get(by_id)

    @classmethod
    def find_or_404(cls, by_id):
        """ Find a Promotions by it's id """
        logger.info("Processing lookup or 404 for id %s ...", by_id)
        return cls.query.get_or_404(by_id)

    @classmethod
    def find_by_name(cls, name):
        """Returns all Promotionss with the given name

        Args:
            name (string): the name of the Promotionss you want to match
        """
        logger.info("Processing name query for %s ...", name)
        return cls.query.filter(cls.name == name)
