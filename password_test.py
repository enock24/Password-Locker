import unittest
from password import User , Credential


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Towett", "enock24", "enock2470")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name, "Towett")
        self.assertEqual(self.new_user.username, "enock24")
        self.assertEqual(self.new_user.password, "enock2470")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''

        self.new_user.save_user()
        test_user = User("Towett", "enock24", "enock2470")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''

        self.new_user.save_user()
        test_user = User("Towett", "enock24", "enock2470")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by name and display information
        '''

        self.new_user.save_user()
        test_user = User("Towett", "enock24", "enock2470")
        test_user.save_user()

        found_user = User.find_user_by_name("Towett")

        self.assertEqual(found_user.username,test_user.username) 

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Towett", "enock24", "enock2470")
        test_user.save_user()
        
        user_exists = User.user_exist("Towett")

        self.assertTrue(user_exists)

    class TestCredential(unittest.TestCase):
        def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_credential = Credential("Towett","twitter", "enock24","enock2470")

        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_credential.name,"Towett")
            self.assertEqual(self.new_credential.account,"twitter")
            self.assertEqual(self.new_credential.username,"enock24")
            self.assertEqual(self.new_credential.password,"enock2470")   

        def test_save_credential(self):
            '''
            test_save_credential test case to test if the user object is saved into
            the credential list
            '''
            self.new_credential.save_credential() # saving the new credential
            self.assertEqual(len(Credential.credential_list),1)

        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []  

        def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Towett","twitter","enock24","enock2470") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2) 

        def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Towett","twitter","enock24","enock2470") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)
 

     



