import unittest
import database


class TestDatabase(unittest.TestCase):

    def test_get_all_posts_returns_posts(self):
        posts = database.get_all_posts()
        self.assertGreaterEqual(len(posts), 1)

    def test_get_post_returns_post(self):
        post = database.get_post(1)
        self.assertIsNotNone(post)

    def test_get_tags_for_post_returns_list(self):
        tags = database.get_tags_for_post(1)
        self.assertIsNotNone(tags)
    
    def test_get_comments_for_post_returns_list(self):
        comments = database.get_comments_for_post(1)
        self.assertIsNotNone(comments)


if __name__ == "__main__":
    unittest.main()