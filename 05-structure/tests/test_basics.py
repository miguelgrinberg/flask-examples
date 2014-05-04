import unittest
from flask import current_app
from app import create_app, mongo


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        for c in mongo.db.collection_names(False):
            print(c)
            mongo.db.drop_collection(c)
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_names(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'What is your name?' in response.data)

        response = self.client.post('/', data={'name': 'dave'})
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'Hello, dave' in response.data)
        self.assertTrue(b'Nice to meet you' in response.data)

        response = self.client.post('/', data={'name': 'dave'})
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'Hello, dave' in response.data)
        self.assertTrue(b'Great to see you again' in response.data)
