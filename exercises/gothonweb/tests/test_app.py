from unittest import TestCase

from app import app

app.config['TESTING'] = True
web = app.test_client()


class TestApp(TestCase):

    def test_index(self):
        rv = web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
