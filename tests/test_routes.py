import unittest
from app import app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Latest Posts", response.data)
    
    def test_new_post_page_loads(self):
        response = self.client.get("/posts/new")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create New Blog Post", response.data)

if __name__ == "__main__":
    unittest.main()