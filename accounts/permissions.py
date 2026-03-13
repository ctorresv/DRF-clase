from rest_framework import permissions

class IsNotAuthenticated(permissions.BasePermission):
    """
    Permite el acceso solo a usuarios NO autenticados.
    Útil para vistas de registro y login.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated
            