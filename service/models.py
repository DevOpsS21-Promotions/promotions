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
    Class that represents a Promotion
    """

    app = None

    ##################################################
    # Table Schema
    ##################################################
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63), nullable=False)
    description = db.Column(db.String(140), nullable=False)
    promo_code = db.Column(db.String(63), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

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
    
    def update(self):
        """
        Updates a promotion to the data store
        """
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        """ Removes a Promotions from the data store """
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """ Serializes a Promotions into a dictionary """
        return {
             "id": self.id, 
             "name": self.name,
             "description": self.description,
             "promo_code": self.promo_code,
             "start_date": datetime.strftime(self.start_date, DATETIME),
             "end_date": datetime.strftime(self.end_date, DATETIME),
             "is_active": self.is_active
        }

    def deserialize(self, data):
        """
        Deserializes a Promotions from a dictionary

        Args:
            data (dict): A dictionary containing the resource data
        """
        try:
            self.name = data["name"]
            self.description = data["description"]
            self.promo_code = data["promo_code"]
            self.start_date = datetime.strptime(data["start_date"], DATETIME)
            self.end_date = datetime.strptime(data["end_date"], DATETIME)
            self.is_active = data["is_active"]
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
