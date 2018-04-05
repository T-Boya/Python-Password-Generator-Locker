import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.newUser = User("www.google.com", "Joe", "Joes")

    def tearDown(self):
        User.UserAccounts = []

    def test_init(self):
        self.assertEqual(self.newUser.website, "www.google.com")
        self.assertEqual(self.newUser.username, "Joe")
        self.assertEqual(self.newUser.password, "Joes")

    def test_save_user(self):
        self.newUser.save_user()
        self.assertEqual(len(User.UserAccounts),1)

    def test_multiple_instances(self):
        self.newUser.save_user()
        test_user = User("www.google.com", "Joe", "Joes")
        test_user.save_user()
        self.assertEqual(len(User.UserAccounts),2)

    def test_delete_account(self):
        self.newUser.save_user()
        test_user = User("www.google.com", "Joe", "Joes")
        test_user.save_user()
        self.newUser.deleteUser()
        self.assertEqual(len(User.UserAccounts), 1)

    def test_usernameLookup(self):
        self.newUser.save_user()
        test_user = User("www.google.com", "Joe", "Joes")
        test_user.save_user()
        searchedUser = User.find_by_username(User, "Joe")
        self.assertEqual(searchedUser.username, test_user.username)

    def test_user_exist(self):
        self.newUser.save_user()
        test_user = User("www.google.com", "Joe", "Joes")
        test_user.save_user()
        user_exists = User.userFound(User, "Joe")
        self.assertTrue(user_exists)

    def test_display(self):
        self.assertEqual(User.displayCredentials(), User.UserAccounts)


if __name__=="__main__":
    unittest.main()