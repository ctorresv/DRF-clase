""" import factory
from .models import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        titulo = "Post Random"
        contenido = "Contenido Random"     """