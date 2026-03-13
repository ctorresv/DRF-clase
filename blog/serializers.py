# serializers.py
from rest_framework import serializers
from .models import Post, Categoria, Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comentario
        fields = ['id', 'autor', 'contenido', 'creado']
        read_only_fields = ['autor']
        
class PostSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(read_only=True) # Muestra el nombre del autor en vez del ID
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'contenido', 'autor', 'categoria', 'comentarios']
        read_only_fields = ['autor']
