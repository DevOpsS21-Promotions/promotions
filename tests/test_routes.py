"""
TestYourResourceModel API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch
from flask_api import status  # HTTP Status Codes
from service.models import db
from service.routes import app, init_db
from datetime import datetime

DATETIME = "%Y-%m-%d %H:%M:%S"

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  T E S T   C A S E S
######################################################################
class TestYourResourceServer(TestCase):
    """ REST API Server Tests """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        pass

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        """ This runs before each test """
        self.app = app.test_client()

    def tearDown(self):
        """ This runs after each test """
        pass

    ######################################################################
    #  P L A C E   T E S T   C A S E S   H E R E
    ######################################################################

    def test_index(self):
        """ Test index call """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_promotion(self):
        """ Test create promotion"""
        promotion = Promotions(name="Test",
                        description="Testing Promotion",
                        promo_code="ABC123",
                        start_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                        end_date=datetime.strptime('2022-01-01 00:00:00', DATETIME),
                        modified_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                        created_date=datetime.strptime('2021-01-01 00:00:00', DATETIME),
                        is_active=True)
        resp = self.app.get("/promotions")
                resp = self.app.post(
            BASE_URL, json=promotion.serialize(), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # Make sure location header is set
        location = resp.headers.get("Location", None)
        self.assertTrue(location != None)
        # Check the data is correct
        new_promotion = resp.get_json()
        self.assertEqual(new_promotion["name"], promotion.name, "Names do not match")
        self.assertEqual(new_promotion["description"], promotion.description, "Description do not match")
        self.assertEqual(new_promotion["promo_code"], promotion.promo_code, "Promo Code does not match")
        self.assertEqual(datetime.strptime(new_promotion["start_date"], DATETIME), datetime.strptime(promotion.start_date, DATETIME), "Start dates do not match")
        self.assertEqual(datetime.strptime(new_promotion["end_date"], DATETIME), datetime.strptime(promotion.end_date, DATETIME), "End dates do not match")
        self.assertEqual(datetime.strptime(new_promotion["modified_date"], DATETIME), datetime.strptime(promotion.modified_date, DATETIME), "Modified dates do not match")
        self.assertEqual(datetime.strptime(new_promotion["created_date"], DATETIME), datetime.strptime(promotion.create_date, DATETIME), "Created dates do not match")
        self.assertEqual(new_promotion["is_avitve"], promotion.is_active, "Is Active does not match")
    
        # TODO: When get promotion is implemented
        # Check that the location header was correct
        #resp = self.app.get(location, content_type=CONTENT_TYPE_JSON)
        #self.assertEqual(resp.status_code, status.HTTP_200_OK)
        #new_promotion = resp.get_json()
        #self.assertEqual(new_promotion["name"], promotion.name, "Names do not match")
        #self.assertEqual(new_promotion["description"], promotion.description, "Description do not match")
        #self.assertEqual(new_promotion["promo_code"], promotion.promo_code, "Promo Code does not match")
        #self.assertEqual(datetime.strptime(new_promotion["start_date"], DATETIME), datetime.strptime(promotion.start_date, DATETIME), "Start dates do not match")
        #self.assertEqual(datetime.strptime(new_promotion["end_date"], DATETIME), datetime.strptime(promotion.end_date, DATETIME), "End dates do not match")
        #self.assertEqual(datetime.strptime(new_promotion["modified_date"], DATETIME), datetime.strptime(promotion.modified_date, DATETIME), "Modified dates do not match")
        #self.assertEqual(datetime.strptime(new_promotion["created_date"], DATETIME), datetime.strptime(promotion.create_date, DATETIME), "Created dates do not match")
        #self.assertEqual(new_promotion["is_avitve"], promotion.is_active, "Is Active does not match")

    def test_delete_promotion(self):
        """ Test delete promotion"""
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_promotion(self):
        """ Test get promotion"""
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_all_promotion(self):
        """ Test get all promotion"""
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_update_promotion(self):
        """ Test update promotion"""
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
