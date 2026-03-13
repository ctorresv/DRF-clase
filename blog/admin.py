from django.contrib import admin

# Register your models here.
from .models import Post, Categoria

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo','autor', 'publicado']


admin.site.register(Categoria)