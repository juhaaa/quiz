import unittest
from services.question_services import question_service
from services.question_services import additional_answers
from services.question_services import more_additional_answers
from services.connection_services import get_db_connection

class TestQuestionServices(unittest.TestCase):
    
    def setUp(self):
        self.connection = get_db_connection()

    # Test for initial database query
    # Should return list with country name, cca2- code
    # and capital city

    def test_get_country(self):
        data = question_service(self.connection)
        self.assertIsInstance(data, list)

    # Test that len of tuple (data[0] == 3)

    def test_list_len(self):
        data = question_service(self.connection)
        l = len(data[0])
        self.assertEqual(l, 3)

    # Test with cca2 countrycode where there is at least 3 
    # cities in the database (FI)

    def test_additional_answers(self):
        data = additional_answers("FI", self.connection)
        l = len(data)
        self.assertEqual(l, 3)

    # Test with a country with less than 3 cities in database (MC)    
    
    def test_more_additional_answers(self):
        data = additional_answers("MC", self.connection)
        l = len(data)
        self.assertEqual(l, 3)
