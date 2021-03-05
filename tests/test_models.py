"""
Test cases for Promotions Model

"""
import logging
import unittest
import os
from service.models import Promotions, DataValidationError, db

######################################################################
#  <your resource name>   M O D E L   T E S T   C A S E S
######################################################################
class TestPromotions(unittest.TestCase):
    """ Test Cases for Promotions Model """

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
        pass

    def tearDown(self):
        """ This runs after each test """
        pass

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
        self.assertTrue(True)

   def test_deserialize_promotion(self):
        """ Test Deserialize Promotion """
        self.assertTrue(True)

   def test_find_by_name(self):
        """ Find a Promotion by Name """
        self.assertTrue(True)

   def test_find_or_404_found(self):
        """ Find or return 404 found """
        self.assertTrue(True)

