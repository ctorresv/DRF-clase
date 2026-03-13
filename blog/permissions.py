# permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.autor == request.user

class IsAutorGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permitir lectura a todos, escritura solo a autores
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Autor').exists()
    
