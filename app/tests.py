import unittest

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_fetch_home(self):
        response = self.app.get("/home")
        self.assertEqual(response.status_code, 200)

    def test_fetch_topics_trending(self):
        response = self.app.get("/topics/trending")
        self.assertEqual(response.status_code, 200)

    def test_fetch_topic_new(self):
        response = self.app.get("/topics/new")
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_categories(self):
        response = self.app.get("/categories")
        self.assertEqual(response.status_code, 200)

    def test_fetch_recent(self):
        response = self.app.get("/posts/recent")
        self.assertEqual(response.status_code, 200)
    
    def test_search(self):
        import random
        search_terms = ['buhari', 'trump', 'bbnaija', 'tacha']
        response = self.app.post("/search", data={'term' : random.choice(search_terms)})
        self.assertEqual(response.status_code, 200)

    def test_fetch_user(self):
        import random
        search_terms = ['seun', 'bolaji21', 'olatorich']
        response = self.app.get("/users/"+random.choice(search_terms))
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_user_posts(self):
        import random
        search_terms = ['seun', 'bolaji21', 'olatorich']
        response = self.app.get("/users/"+random.choice(search_terms)+"/posts")
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_topics(self):
        import random
        search_terms = ['seun', 'bolaji21', 'olatorich']
        response = self.app.get("/users/"+random.choice(search_terms)+"/topics")
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_category_topics(self):
        response = self.app.get("/categories/politics/topics")
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_topic_post(self):
        import random
        search_terms = [5459935, 5459903, 5459832]
       
        response = self.app.get("/topics/"+str(random.choice(search_terms))+"/posts")
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_followed_topics(self):
        response = self.app.get("/user/followed_topics")
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_followed_boards(self):
        response = self.app.get("/user/followed_boards")
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_mentions(self):
        response = self.app.get("/user/mentions")
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_followed_posts(self):  
        response = self.app.get("/user/following_posts")
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_posts_shared_with(self):
        response = self.app.get("/user/shared_with")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()