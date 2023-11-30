import unittest
from app import app

class TestReferenceForm(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_form_submission_with_valid_inputs(self):
        response = self.app.post("/add", data=dict(
            tag="some tag",
            title="some title",
            author="some author",
            publish_year=2000,
            publisher="some publiser"

        ))

        self.assertEqual(response.status_code, 200)

    def test_form_submission_with_whitespace(self):
        response = self.app.post("/add", data=dict(
            tag="some tag",
            title="  some title",
            author="some author",
            publish_year=2000,
            publisher="some publiser"   

        ))

        self.assertIn(b"Remove leading or trailing spaces", response.data)
        self.assertIn(b'required', response.data)
