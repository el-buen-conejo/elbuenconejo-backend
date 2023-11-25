from rest_framework.viewsets import ModelViewSet
from apps.profiles.api.serializer import ProfileSerializer, ProfilePhotoSerializer
from utils.pagination import ExtendedPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from utils.filters import ProfileFilterSet


class ProfileModelViewSet(ModelViewSet): 
    serializer_class = ProfileSerializer
    pagination_class = ExtendedPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = ProfileFilterSet

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(is_active=True).order_by(
            "last_name"
        )

    @extend_schema(request=ProfilePhotoSerializer, responses=ProfilePhotoSerializer)
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        profile = self.get_object()
        serializer = ProfilePhotoSerializer(
            instance=profile, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
