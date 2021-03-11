"""
Test cases for Promotions Model

"""
import logging
import unittest
import os
from service.models import Promotions, DataValidationError, db
from service import app
from datetime import datetime

DATETIME = "%Y-%m-%d %H:%M:%S"

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  <your resource name>   M O D E L   T E S T   C A S E S
######################################################################
class TestPromotions(unittest.TestCase):
    """ Test Cases for Promotions Model """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Promotions.init_db(app)

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_promotion(self):
        """ Test Create Promotion """
        self.assertTrue(True)

    def test_find_promotion(self):
        """ Test Find Promotion """
        self.assertTrue(True)

    def test_update_promotion(self):
        """ Test Update Promotion """
        self.assertTrue(True)

    def test_delete_promotion(self):
        """ Test Delete Promotion """
        self.assertTrue(True)

    def test_serialize_promotion(self):
        """ Test Serialize Promotion """
        promotion = Promotions(name="Test",
                               description="Testing Promotion",
                               promo_code="ABC123",
                               start_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               end_date=datetime.strptime('2022-01-01 00:00:00', DATETIME),
                               modified_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               created_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               is_active=True)
        data = promotion.serialize()
        self.assertNotEqual(data, None)
        self.assertIn("id", data)
        self.assertEqual(data["id"], None)
        self.assertIn("name", data)
        self.assertEqual(data["name"], "Test")
        self.assertIn("description", data)
        self.assertEqual(data["description"], "Testing Promotion")
        self.assertIn("promo_code", data)
        self.assertEqual(data["promo_code"], "ABC123")
        self.assertIn("start_date", data)
        self.assertEqual(datetime.strptime(data["start_date"], DATETIME), datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertIn("end_date", data)
        self.assertEqual(datetime.strptime(data["end_date"], DATETIME), datetime.strptime('2022-01-01 00:00:00', DATETIME))
        self.assertIn("modified_date", data)
        self.assertEqual(datetime.strptime(data["modified_date"], DATETIME), datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertIn("created_date", data)
        self.assertEqual(datetime.strptime(data["created_date"], DATETIME), datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertIn("is_active", data)
        self.assertEqual(data["is_active"], True)

    def test_deserialize_promotion(self):
        """ Test Deserialize Promotion """
        promotion = Promotions(name="Test",
                               description="Testing Promotion",
                               promo_code="ABC123",
                               start_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               end_date=datetime.strptime('2022-01-01 00:00:00', DATETIME),
                               modified_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               created_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               is_active=True)
        data = promotion.serialize()
        promotion.deserialize(data)
        self.assertNotEqual(promotion, None)
        self.assertEqual(promotion.id, None)
        self.assertEqual(promotion.name, "Test")
        self.assertEqual(promotion.description, "Testing Promotion")
        self.assertEqual(promotion.promo_code, "ABC123")
        self.assertEqual(promotion.start_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotion.end_date, datetime.strptime('2022-01-01 00:00:00', DATETIME))                               
        self.assertEqual(promotion.modified_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotion.created_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotion.is_active, True)             

    def test_find_by_name(self):
        """ Find a Promotion by Name """
        self.assertTrue(True)

    def test_find_or_404_found(self):
        """ Find or return 404 found """
        self.assertTrue(True)

