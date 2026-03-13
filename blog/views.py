from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comentario
from .serializers import PostSerializer, ComentarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

#ViewSets
#cambio
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAutorGroup, IsOwnerOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    queryset=Post.objects.select_related('autor')\
.prefetch_related('comentarios')
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsAutorGroup, IsOwnerOrReadOnly] 
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = PostFilter
    search_fields = ['titulo', 'contenido']
    ordering_fields = ['creado', 'actualizado', 'titulo']
    ordering = ['-creado']  # por defecto: más recientes primero
    
    def list(self, request, *args, **kwargs):
        # Validar parámetros
        page_size = request.query_params.get('page_size')
        if page_size and not page_size.isdigit():
            raise ValidationError({'page_size': 'Debe ser un número'})
        if page_size and int(page_size) > 100:
            raise ValidationError({'page_size': 'Máximo 100 por página'})
        
        return super().list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
    
""" 
GET ver lista de post /api/posts/
POST Crear un post    /api/posts/
GET Ver detalles      /api/posts/<pk>
PUT editar            /api/posts/<pk>
DELETE Eliminar post  /api/posts/<pk>
 
"""

class ComentarioViewSet(ModelViewSet):
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comentario.objects.select_related('autor')\
                             .filter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post_id = self.kwargs['post_pk']
        serializer.save(autor=self.request.user, post_id=self.kwargs['post_pk'])