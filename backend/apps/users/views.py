from apps.users.api.serializers import (
    CustomTokenObtainPairSerializer,
    CustomUserSerializer,
)
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, serializers


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(username=username, password=password)
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response(
                    {
                        "token": login_serializer.validated_data.get("access"),
                        "refresh-token": login_serializer.validated_data.get("refresh"),
                        "user": user_serializer.data.get("username"),
                        "id": user_serializer.data.get("id"),
                        "message": "Inicio de Sesión Exitoso.",
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Contraseña o nombre de usuario incorrectos."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"error": "Contraseña o nombre de usuario incorrectos."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class EmptySerializer(serializers.Serializer):
    pass


class Logout(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmptySerializer  # We use the empty serializer

    def post(self, request, *args, **kwargs):
        if self.request.data.get("all"):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)

            return Response(
                {"message": "OK, adios, todos los refresh token estan en lista negra"},
                status=status.HTTP_204_NO_CONTENT,
            )

        refresh_token = self.request.data.get("refresh_token")
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response(
            {"message": "Sesión cerrada exitosamente"},
            status=status.HTTP_204_NO_CONTENT,
        )
