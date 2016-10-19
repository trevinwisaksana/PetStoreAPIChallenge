
'''
Topic: Unit Testing
Unit tests are only done on very specific contents
of the code. This test is only tests that it
returns what we expect it to return.
'''
# Imported unittest
import unittest
# Imported server
import petStoreAPIChallenge as server
# Imported JSON
import json
# Imported Flask
from flask import Flask


class FlaskServerTest(unittest.TestCase):
    """docstring for FlaskServerTest."""
    def setUp(self):
        # Run app in testing mode to retrieve exceptions and stack traces
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        # Making a request to my local server
        response = self.app.get('/hello')
        # Response status: Would fail if the value is not true
        assert response.status_code == 200, "status_code was not OK"
        print(response.data.decode())
        assert response.data.decode() == "Hello, World!"


if __name__ == '__main__':
    unittest.main()
