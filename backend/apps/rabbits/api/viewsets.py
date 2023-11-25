from rest_framework import viewsets, status, filters
from apps.rabbits.models import Rabbit
from utils.filters import RabbitFilterSet
from utils.pagination import RabbitPagination
from apps.rabbits.api.serializers import RabbitSerializer, RabbitPhotoSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from utils.permisssions import ListAndRetrievePermission


class RabbitViewSet(viewsets.ModelViewSet):
    queryset = Rabbit.objects.filter(is_active=True).order_by("-created") 
    serializer_class = RabbitSerializer
    pagination_class = RabbitPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = RabbitFilterSet
    read_only_fields = (
        "created",
        "id",
        "age",
        "tag",
    )
    permission_classes = [ListAndRetrievePermission]

    def get_queryset(self):
        queryset = Rabbit.objects.filter(is_active=True)

        created = self.request.query_params.get("created")
        breed = self.request.query_params.get("breed")
        genre = self.request.query_params.get("genre")
        birthday = self.request.query_params.get("birthday")
        price = self.request.query_params.get("price")
        tag = self.request.query_params.get("tag")
        weight = self.request.query_params.get("weight")
        cage_id = self.request.query_params.get("cage_id")
        is_active = self.request.query_params.get("is_active")

        filters = Q()

        if created:
            filters &= Q(created__icontains=created)
        if breed:
            filters &= Q(breed__icontains=breed)
        if genre:
            filters &= Q(genre__icontains=genre)
        if birthday:
            filters &= Q(birthday__icontains=birthday)
        if price:
            filters &= Q(price=price)
        if tag:
            filters &= Q(tag__icontains=tag)
        if weight:
            filters &= Q(weight=weight)
        if cage_id:
            filters &= Q(cage_id=cage_id)
        if is_active:
            if is_active.lower() == "true":
                filters &= Q(is_active=True)
            elif is_active.lower() == "false":
                filters &= Q(is_active=False)

        queryset = queryset.filter(filters)

        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = RabbitSerializer(instance, data=request.data, partial=partial)

        # Check if the updated field is read-only
        for field in self.read_only_fields:
            if field in request.data:
                return Response(
                    {
                        "error": f"No puedes actualizar el campo de solo lectura <<'{field}'>>"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):   
        rabbit_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).first()
        if rabbit_destroy:
            serializer = self.get_serializer(rabbit_destroy)
            serializer.delete(rabbit_destroy)
            return Response(
                {"message": "Conejo eliminado correctamente"},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {"message": "El conejo no existe"}, status=status.HTTP_404_NOT_FOUND
        )

    @extend_schema(request=RabbitPhotoSerializer, responses=RabbitPhotoSerializer)
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        rabbit = self.get_object()
        serializer = RabbitPhotoSerializer(
            instance=rabbit, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example Schema",
                {
                    "breed": "Azteca",
                    "genre": "Macho",
                    "birthday": "2023-10-31",
                    "tag": "AB123",
                    "price": "500",
                    "weight": "6",
                    "cage_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                },
            )
        ],
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
