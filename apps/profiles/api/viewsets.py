from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.profiles.api.serializer import ProfilePhotoSerializer, ProfileSerializer
from utils.filters import ProfileFilterSet
from utils.pagination import ExtendedPagination
from utils.upload import upload_image_to_cloudinary


class ProfileModelViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    pagination_class = ExtendedPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = ProfileFilterSet
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.order_by("last_name")

    @extend_schema(
        request=ProfilePhotoSerializer,
        responses=ProfilePhotoSerializer,
        examples=[
            OpenApiExample(
                "Photo upload",
                value={"photo": "image.jpeg"},
                media_type="multipart/form-data",
            )
        ],
    )
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        profile = self.get_object()

        # Verify if the user is the owner of the profile
        if profile.user_id != request.user:
            return Response(
                {"detail": "No tiene permiso para modificar este perfil."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ProfilePhotoSerializer(
            instance=profile, data=request.data, partial=True
        )
        if serializer.is_valid():
            photo_file = request.FILES.get("photo")

            if not photo_file:
                return Response(
                    {"detail": "No se ha proporcionado una imagen válida."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Upload the image to Cloudinary

            upload_url = upload_image_to_cloudinary(photo_file, target="fotos/perfiles")
            request.data["photo"] = upload_url

            # Save the image url uploaded to Cloudinary
            self.perform_update(serializer)

            print("--" * 50)
            print(f"Imagen: {upload_url}")

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
