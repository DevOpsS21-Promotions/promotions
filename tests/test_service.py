"""
TestYourResourceModel API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import unittest
import os
import unittest
import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch
from flask_api import status  # HTTP Status Codes
from service.models import db, Promotions
from service.routes import app, init_db
from datetime import datetime
import json

DATETIME = "%Y-%m-%d %H:%M:%S"
CONTENT_TYPE_JSON = "application/json"
DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  T E S T   C A S E S
######################################################################
class TestPromotionsService(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        init_db()


    def setUp(self):
        """ This runs before each test """
        db.drop_all()  # clean up the last tests
        db.create_all()  # create new tables
        self.app = app.test_client()

    def tearDown(self):
        """ This runs after each test """
        db.session.remove()
        db.drop_all()

    ######################################################################
    #  HELPER FUNCTIONS
    ######################################################################

    def _create_promotion(self):
        return Promotions(name="Test",
                          description="Testing Promotion",
                          promo_code="ABC123",
                          start_date=datetime.strptime("2021-01-01 00:00:00", DATETIME),
                          end_date=datetime.strptime("2022-01-01 00:00:00", DATETIME),
                          is_active=True
        )

    def _create_and_post_promotion(self):
        test_promotion = self._create_promotion()
        resp = self.app.post(
            "/promotions", json=test_promotion.serialize(), content_type=CONTENT_TYPE_JSON
        )        
        new_promotion = resp.get_json()
        test_promotion.id = new_promotion["id"]
        return test_promotion

    ######################################################################
    #  TEST CASES
    ######################################################################

    def test_index(self):
        """ Test index call """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_promotion(self):
        """ Test create promotion"""
        
        promotion = self._create_promotion()
        resp = self.app.post(
            "/promotions", json=promotion.serialize(), content_type=CONTENT_TYPE_JSON
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
        self.assertEqual(datetime.strptime(new_promotion["start_date"], DATETIME), promotion.start_date, "Start dates do not match")
        self.assertEqual(datetime.strptime(new_promotion["end_date"], DATETIME), promotion.end_date, "End dates do not match")
        self.assertEqual(new_promotion["is_active"], promotion.is_active, "Is Active does not match")
    
        # Check that the location header was correct
        resp = self.app.get(location, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        new_promotion = resp.get_json()
        self.assertEqual(new_promotion["name"], promotion.name, "Names do not match")
        self.assertEqual(new_promotion["description"], promotion.description, "Description do not match")
        self.assertEqual(new_promotion["promo_code"], promotion.promo_code, "Promo Code does not match")
        self.assertEqual(datetime.strptime(new_promotion["start_date"], DATETIME), promotion.start_date, "Start dates do not match")
        self.assertEqual(datetime.strptime(new_promotion["end_date"], DATETIME), promotion.end_date, "End dates do not match")
        self.assertEqual(new_promotion["is_active"], promotion.is_active, "Is Active does not match")

    def test_create_promotion_bad_request(self):
        """ Create a Promotion Bad Request"""
        resp = self.app.post(
            "/promotions", data="bad request", content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_promotion(self):
        """ Test delete promotion"""
        test_promotion = self._create_and_post_promotion()
        resp = self.app.delete(
            "/promotions/{}".format(test_promotion.id), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(resp.data), 0)
        # make sure they are deleted
        resp = self.app.get(
            "/promotions/{}".format(test_promotion.id), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_promotion(self):
        """ Test get promotion"""
        # get the id of a promotion
        test_promotion = self._create_and_post_promotion()
        resp = self.app.get(
            "/promotions/{}".format(test_promotion.id), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(data["name"], test_promotion.name)

    def test_get_account_not_found(self):
        """ Get an Promotion that is not found """
        resp = self.app.get("/promotions/0")
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_all_promotion(self):
        """ Test get all (list) promotion"""
        self._create_and_post_promotion()
        self._create_and_post_promotion()
        resp = self.app.get("/promotions")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(len(data), 2)

    def test_update_promotion(self):
        """ Test update promotion"""
        test_promotion = self._create_promotion()
        resp = self.app.post(
            "/promotions", json=test_promotion.serialize(), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # update the promotion
        new_promotion = resp.get_json()
        new_promotion["description"] = "Updated Description"
        resp = self.app.put(
            "{0}/{1}".format("/promotions", new_promotion["id"]),
            json=new_promotion,
            content_type=CONTENT_TYPE_JSON,
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        updated_promotion = resp.get_json()
        self.assertEqual(updated_promotion["description"], "Updated Description")

    def test_cancel_promotion(self):
        """ Test cancel promotion"""
        test_promotion = self._create_promotion()
        resp = self.app.post(
            "/promotions", json=test_promotion.serialize(), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # cancel the promotion
        cancel_promotion = resp.get_json()
        resp = self.app.put(
            "{0}/{1}/{2}".format("/promotions/", cancel_promotion["id"], "/cancel"),
            content_type=CONTENT_TYPE_JSON,
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        canceled_promotion = resp.get_json()
        self.assertEqual(canceled_promotion["is_active"], False)

    def test_unsupported_media_type(self):
        """ Send wrong media type """
        promotion = self._create_promotion()
        resp = self.app.post(
            "/promotions", 
            json=promotion.serialize(), 
            content_type="test/html"
        )
        self.assertEqual(resp.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    def test_method_not_allowed(self):
        """ Make an illegal method call """
        resp = self.app.put(
            "/promotions", 
            json={"not": "today"}, 
            content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
