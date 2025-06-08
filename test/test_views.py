import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
import json

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        self.assertEqual(rv.status_code, 200)
        for fmt in SUPPORTED:
            self.assertIn(fmt, rv.data.decode())

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(rv.status_code, 200)

        data = json.loads(rv.data.decode())
        self.assertEqual(data, {"imie": "Tomasz", "msg": "Hello World!"})