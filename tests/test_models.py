"""
Test cases for Promotions Model

"""
import logging
import unittest
import os
from service.models import Promotions, DataValidationError, db
from service import app
from datetime import datetime
from werkzeug.exceptions import NotFound

DATETIME = "%Y-%m-%d %H:%M:%S"

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.environ['VCAP_SERVICES'])
    DATABASE_URI = vcap['user-provided'][0]['credentials']['url']

######################################################################
#  Promotions   M O D E L   T E S T   C A S E S
######################################################################
class TestPromotions(unittest.TestCase):
    """ Test Cases for Promotions Model """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        global DATABASE_URI
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        if 'VCAP_SERVICES' in os.environ:
            vcap = json.loads(os.environ['VCAP_SERVICES'])
            DATABASE_URI = vcap['user-provided'][0]['credentials']['url']
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

    def _create_promotion(self):
        return Promotions(name="Test",
                               description="Testing Promotion",
                               promo_code="ABC123",
                               start_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                               end_date=datetime.strptime('2022-01-01 00:00:00', DATETIME),
                               is_active=True
        )

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_promotion(self):
        """ Test Create Promotion """
        promotion = self._create_promotion()
        self.assertTrue(promotion != None)
        self.assertEqual(promotion.id, None)
        self.assertEqual(promotion.name, "Test")
        self.assertEqual(promotion.description, "Testing Promotion")
        self.assertEqual(promotion.promo_code, "ABC123")
        self.assertEqual(promotion.start_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotion.end_date, datetime.strptime('2022-01-01 00:00:00', DATETIME))                               
        self.assertEqual(promotion.is_active, True)

    def test_add_promotion(self):
        """ Test Add Promotion to database"""
        test_promotion = Promotions.all()
        self.assertEqual(test_promotion, [])
        test_promotion = self._create_promotion()
        self.assertTrue(test_promotion != None)
        self.assertEqual(test_promotion.id, None)
        test_promotion.create()
        # Asert that it was assigned an id and shows up in the database
        self.assertEqual(test_promotion.id, 1)
        test_promotion = Promotions.all()
        self.assertEqual(len(test_promotion), 1)        

    def test_find_promotion(self):
        """ Test Find Promotion """
        test_promotion = self._create_promotion()
        test_promotion.create()
        promotion = Promotions.find(test_promotion.id)
        self.assertEqual(promotion.id, test_promotion.id)
        self.assertEqual(promotion.name, "Test")
        self.assertEqual(promotion.description, "Testing Promotion")
        self.assertEqual(promotion.promo_code, "ABC123")
        self.assertEqual(promotion.start_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotion.end_date, datetime.strptime('2022-01-01 00:00:00', DATETIME))                               
        self.assertEqual(promotion.is_active, True)


    def test_update_promotion(self):
        """ Test Update Promotion """
        test_promotion = self._create_promotion()
        test_promotion.create()
        self.assertEqual(test_promotion.id, 1)
        # Change it an update it
        test_promotion.description = "Updated Description"
        test_promotion.update()
        self.assertEqual(test_promotion.id, 1)
        # Fetch it back and make sure the id hasn't changed
        # but the data did change
        test_promotion = Promotions.all()
        self.assertEqual(len(test_promotion), 1)
        self.assertEqual(test_promotion[0].description, "Updated Description")

    def test_delete_promotion(self):
        """ Test Delete Promotion """
        test_promotion = self._create_promotion()
        test_promotion.create()
        self.assertEqual(len(Promotions.all()), 1)
        # delete the pet and make sure it isn't in the database
        test_promotion.delete()
        self.assertEqual(len(Promotions.all()), 0)
        

    def test_serialize_promotion(self):
        """ Test Serialize Promotion """
        promotion = self._create_promotion()
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
        self.assertIn("is_active", data)
        self.assertEqual(data["is_active"], True)

    def test_deserialize_promotion(self):
        """ Test Deserialize Promotion """
        promotion = self._create_promotion()
        data = promotion.serialize()
        promotion.deserialize(data)
        self.assertNotEqual(promotion, None)
        self.assertEqual(promotion.id, None)
        self.assertEqual(promotion.name, "Test")
        self.assertEqual(promotion.description, "Testing Promotion")
        self.assertEqual(promotion.promo_code, "ABC123")
        self.assertEqual(promotion.start_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotion.end_date, datetime.strptime('2022-01-01 00:00:00', DATETIME))                               
        self.assertEqual(promotion.is_active, True)             

    def test_deserialize_bad_promotion_data(self):
        """ Test deserialization of bad promotion data """
        data = "this is not a dictionary"
        promotion = Promotions()
        self.assertRaises(DataValidationError, promotion.deserialize, data)

    def test_find_by_name(self):
        """ Find a Promotion by Name """
        self._create_promotion().create()
        Promotions(name="Second",
                    description="Testing Second Promotion",
                    promo_code="EFG456",
                    start_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                    end_date=datetime.strptime('2022-01-01 00:00:00', DATETIME),
                    is_active=False).create()
        promotions = Promotions.find_by_name("Second")
        self.assertEqual(promotions[0].name, "Second")
        self.assertEqual(promotions[0].description, "Testing Second Promotion")
        self.assertEqual(promotions[0].promo_code, "EFG456")
        self.assertEqual(promotions[0].start_date, datetime.strptime('2021-01-01 00:00:00', DATETIME))
        self.assertEqual(promotions[0].end_date, datetime.strptime('2022-01-01 00:00:00', DATETIME))                               
        self.assertEqual(promotions[0].is_active, False)             

    def test_find_or_404(self):
        """ Find or return 404 """
        self.assertRaises(NotFound, Promotions.find_or_404, 0)

