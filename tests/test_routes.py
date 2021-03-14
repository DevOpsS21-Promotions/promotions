"""
TestYourResourceModel API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import unittest
import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch
from flask_api import status  # HTTP Status Codes
from service.models import db, Promotions, DataValidationError
from .promotion_factory import PromotionsFactory
from service import app
from service.routes import app, init_db

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
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
       # for _ in range(count):
        #    test_promotion = PromotionFactory()
         
         #   resp = self.app.post(
          #      BASE_URL, json=test_pet.serialize(), content_type=CONTENT_TYPE_JSON
           #     )
        #self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

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
        test_promotion = PromotionsFactory()
        resp = self.app.post(
            BASE_URL, json=test_pet.serialize(), content_type=CONTENT_TYPE_JSON
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # update the pet
        new_promotion = resp.get_json()
        new_promotion["description"] = "unknown"
        resp = self.app.put(
            "{0}/{1}".format(BASE_URL, new_promotion["name"]),
            json=new_promotion,
            content_type=CONTENT_TYPE_JSON,
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        updated_promotion = resp.get_json()
        self.assertEqual(updated_promotion["description"], "unknown")