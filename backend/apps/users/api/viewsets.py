from utils.filters import UserFilterSet
from utils.pagination import ExtendedPagination
from apps.users.api.serializers import (
    PasswordSerializer,
    UserListSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ProfileSerializerFromUser,
)
from django.shortcuts import get_object_or_404
from django_filters import rest_framework

from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.profiles.models import Profile
from .permisssions import CreateUserPermission
from django.contrib.auth.hashers import make_password
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = UserFilterSet
    search_fields = ("email", "username")
    ordering_fields = ("email", "username")
    pagination_class = ExtendedPagination
    permission_classes = [CreateUserPermission]

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class.Meta.model.objects.filter(
                is_active=True
            ).values("id", "username", "email")
            return self.queryset

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    @action(methods=["post"], detail=True)
    @extend_schema(
        description="Cambia la contraseña",
        summary="Users",
        request=PasswordSerializer,
        responses=None,
    )
    def set_password(self, request, pk=None):
        """
        Change password
        """
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data["password"])
            user.save()
            return Response(
                {"message": "La contraseña se actualizó correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Ocurrieron errores!", "error": password_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        description="Obtiene una colección de usuarios",
        summary="Users",
        request=UserListSerializer,
        responses=UserListSerializer,
    )
    def list(self, request, *args, **kwargs):
        """
        Get a collection of users
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Crea un usuario con perfil vacío",
        summary="Users",
        examples=[
            OpenApiExample(
                "Example Schema",
                {
                    "username": "string",
                    "email": "user@example",
                    "password": "string",
                    "is_producer": "True",
                },
            )
        ],
    )
    def create(self, request):
        """
        Create an user
        """

        data = request.data
        is_producer = data.get("is_producer", False)
        user_data = {
            "username": data.get("username"),
            "email": data.get("email"),
            "password": make_password(data.get("password")),
        }

        user_serializer = self.serializer_class(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            # Create the profile
            Profile.objects.create(user_id=user, is_producer=is_producer)
            return Response(
                {"message": "El usuario se creo correctamente!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "message": "Hay errores en el registro!",
                "errors": user_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(description="Obtiene el detalle de un usuario", summary="Users")
    def retrieve(self, request, pk=None):
        """
        Get an user
        """
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    @extend_schema(description="Actualiza un usuario", summary="Users")
    def update(self, request, pk=None):
        """
        Update an user
        """
        user = self.get_object(pk)
        user_serializer = UserUpdateSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {"message": "Usuario actualizado correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Hay errores en la actualización!",
                "error": user_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(description="Elimina un usuario en modo lógico", summary="Users")
    def destroy(self, request, pk=None):
        """
        Delete an user in logical mode
        """
        user_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            is_active=False
        )
        if user_destroy == 1:
            return Response(
                {"message": "Usuario eliminado correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "El usuario no existe!"}, status=status.HTTP_404_NOT_FOUND
        )


class ProfileViewSet(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializerFromUser
