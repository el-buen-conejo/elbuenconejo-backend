from rest_framework import permissions


class ListAndRetrievePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permitir a cualquier usuario realizar una solicitud GET (list o retrieve)
        if view.action == "list" or view.action == "retrieve":
            return True
        # Requiere autenticación para otros métodos
        return request.user and request.user.is_authenticated
