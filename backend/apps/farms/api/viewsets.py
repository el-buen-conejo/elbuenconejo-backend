from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from apps.farms.api.serializer import farmSerializer, FarmPhotoSerializer
from apps.farms.models import Farm
from utils.pagination import FarmPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from drf_spectacular.utils import extend_schema,  OpenApiExample
from utils.permisssions import ListAndRetrievePermission
from utils.filters import FarmFilterSet

"""
    The FarmViewset class is a generic viewset that allows any user to access and manipulate Farm
    objects. It is used to create, retrieve, update, and delete Farm objects using the farmSerializer.
"""


class FarmViewset(viewsets.ModelViewSet):
    queryset = Farm.objects.filter(is_active=True).order_by("-created",)
    serializer_class = farmSerializer
    pagination_class = FarmPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    permission_classes = [ListAndRetrievePermission]
    read_only_fields = (
        "id",
        "created",
    )
    filterset_class = FarmFilterSet 

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example Schema",
                {   "profile_id": "60dda079-2c9c-4c18-b787-d1de9fd45189",
                    "name": "string",
                    "address": "string",
                    "description": "string",
                },
            )
        ],
    )
    def create(self, request, *args, **kwargs):
        """
        The above function creates a new object using the provided request data and saves it using the
        serializer.

        :param request: The `request` parameter is an object that represents the HTTP request made by the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and the request body
        return: The function returns a Response object that contains the serialized data of the created object (json).
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Farm.objects.filter(is_active=True)

        profile_id = self.request.query_params.get("profile_id")
        created = self.request.query_params.get("created")
        name = self.request.query_params.get("name")
        address = self.request.query_params.get("address")
        description = self.request.query_params.get("description")

        filters = Q() 

        if profile_id:
            filters &= Q(profile_id=profile_id)
        if created:
            filters &= Q(created__icontains=created)
        if name:
            filters &= Q(name__icontains=name)
        if address:
            filters &= Q(address__icontains=address)
        if description:
            filters &= Q(description__icontains=description)

        queryset = queryset.filter(filters)

        return queryset
    def retrieve(self, request, pk):
        """
        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and the request body
        :param pk: The "pk" parameter stands for "primary key". It is used to identify a specific object
        in a database. In this context, it is used to retrieve a specific item from the database based
        on its primary key value
        :return:The function retrieves an item and returns its serialized data as a response.
        """
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    @extend_schema(description="Elimina una granja en modo lógico", summary="Farms")
    def destroy(self, request, pk=None):
        """
        Delete a farm in logical mode
        """
        farm_destroy = self.serializer_class.Meta.model.objects.filter(id=pk).update(
            is_active=False
        )
        if farm_destroy == 1:
            return Response(
                {"message": "Granja eliminada correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "La granja no existe!"}, status=status.HTTP_404_NOT_FOUND
        )
        
    @extend_schema(request=FarmPhotoSerializer, responses=FarmPhotoSerializer)
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        farm = self.get_object()
        serializer = FarmPhotoSerializer(instance=farm, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
