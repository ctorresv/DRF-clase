from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=100) #VARCHAR(200)
    contenido = models.TextField()   #TEXT
    publicado = models.BooleanField(default=True) #BOOLEAN
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    
    def __str__(self):
        return self.titulo
    
# models.py
class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)