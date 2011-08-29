import unittest
from pymongo import Connection
from mongauth import Mongauth


def get_collection():
    return Connection().mongauth.test

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        auth.obliterate()

    def test_create(self):
        self.assertTrue(auth.new(user,pw))

    def test_no_recreate(self):
        self.assertTrue(auth.new(user,pw))
        self.assertFalse(auth.new(user,pw))
        self.assertFalse(auth.new(user,pw[::-1]))

    def test_recreate(self):
        self.assertTrue(auth.new(user,pw))
        self.assertFalse(auth.new(user,pw))
        self.assertTrue(auth.destroy(user,pw))
        self.assertFalse(auth.destroy(user,pw))
        self.assertTrue(auth.new(user,pw))
        self.assertFalse(auth.new(user,pw))

    def test_admin_recreate(self):
        self.assertTrue(auth.new(user,pw))
        self.assertFalse(auth.new(user,pw))
        self.assertTrue(auth.admin_destroy(user))
        self.assertFalse(auth.admin_destroy(user))
        self.assertTrue(auth.new(user,pw))
        self.assertFalse(auth.new(user,pw))

    def test_other_create(self):
        self.assertTrue(auth.new(user,pw))
        self.assertTrue(auth.new(user[::-1],pw))
        self.assertFalse(auth.new(user,pw))
        self.assertFalse(auth.new(user[::-1],pw))
        
    def test_basic_auth(self):
        self.assertTrue(auth.new(user,pw))
        self.assertTrue(auth.auth(user,pw))
        self.assertTrue(auth.auth(user,pw))

    def test_auth_after_destroy(self):
        self.assertTrue(auth.new(user,pw))
        self.assertTrue(auth.auth(user,pw))
        self.assertTrue(auth.destroy(user,pw))
        self.assertFalse(auth.auth(user,pw))

    def test_recreate_auth_after_destroy(self):
        self.assertTrue(auth.new(user,pw))
        self.assertTrue(auth.auth(user,pw))
        self.assertTrue(auth.destroy(user,pw))
        self.assertFalse(auth.auth(user,pw))
        self.assertTrue(auth.new(user,pw))
        self.assertTrue(auth.auth(user,pw))

if __name__ == "__main__":
    collection = get_collection()
    auth = Mongauth(collection, 12)
    user = "user"
    pw = "secure_password"
    unittest.main()
