# filters.py
import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    contenido = django_filters.CharFilter(lookup_expr='icontains')
    autor = django_filters.CharFilter(field_name='autor__username')
    publicado = django_filters.BooleanFilter()
    categoria = django_filters.CharFilter(field_name='categoria__nombre')
    
    tiene_comentarios = django_filters.BooleanFilter(method='filter_tiene_comentarios')
    
    def filter_tiene_comentarios(self, queryset, name, value):
        if value:
            return queryset.filter(comentarios__isnull=False).distinct()
        return queryset.filter(comentarios__isnull=True)

    class Meta:
        model = Post
        fields = ['titulo', 'contenido','autor', 'publicado', 'categoria','tiene_comentarios']
