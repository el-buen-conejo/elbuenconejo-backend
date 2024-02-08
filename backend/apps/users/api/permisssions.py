from rest_framework import permissions


class CreateUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permitir a cualquier usuario realizar una solicitud POST (create)
        if view.action == "create":
            return True
        # Requiere autenticación para otros métodos
        return request.user and request.user.is_authenticated


class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_producer == False
            and request.method in permissions.SAFE_METHODS
        )


class IsFarmer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_producer == True


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
