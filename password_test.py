import unittest
from password import User , Credential


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Langat", "justo01", "justo1234")
