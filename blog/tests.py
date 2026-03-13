from django.test import TestCase
from .models import Post
#from .factories import PostFactory
from django.test import Client

""" class PostModelTest(TestCase):
    def test_crear_post(self):
        post = PostFactory()
        self.assertEqual(post.titulo, "Post Random")
    

class PostTest(TestCase):
    fixtures = ["posts.json"]
    
    def test_fixture(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.titulo, "Post Fixture") """
        
class PostViewTest(TestCase):
    def test_home(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)