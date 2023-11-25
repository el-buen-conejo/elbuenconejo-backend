from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.cages.api.serializers import CageSerializer, CagePhotoSerializer
from utils.filters import CageFilterSet
from utils.pagination import CagePagination
from apps.cages.models import Cage
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from utils.permisssions import ListAndRetrievePermission


class CageViewSet(viewsets.ModelViewSet):
    queryset = Cage.objects.filter(is_active=True).order_by("-created",)
    serializer_class = CageSerializer

    # custom pagination
    pagination_class = CagePagination

    # search filter and filtering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = CageFilterSet
    search_fields = ["id", "price"]

    # Define fields for ordering
    ordering_fields = ["count_rabbits", "price"]

    read_only_fields = (
        "id",
        "price",
        "count_rabbits",
        "total_weight",
        "created",
    )

    permission_classes = [ListAndRetrievePermission]

    # Range of price filter
    @action(detail=False, methods=["get"])
    def filter_price(self, request):
        price_range = request.query_params.get("price_range")

        try:
            min_price, max_price = map(float, price_range.split("-"))
        except ValueError:
            return Response(
                {
                    "message": "Formato de rango de precios incorrecto. Use el formato 'min-max'."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        queryset = Cage.objects.filter(price__gte=min_price, price__lte=max_price)
        serializer = CageSerializer(queryset, many=True)
        return Response(serializer.data)

    # Search by price
    @action(detail=False, methods=["get"])
    def search_price(self, request):
        price = request.query_params.get("price")
        queryset = Cage.objects.filter(price=price)
        serializer = CageSerializer(queryset, many=True)
        return Response(serializer.data)

    # Search by Count rabbits
    @action(detail=False, methods=["get"])
    def search_count_rabbits(self, request):
        count_rabbits = request.query_params.get("count_rabbits")
        queryset = Cage.objects.filter(count_rabbits=count_rabbits)
        serializer = CageSerializer(queryset, many=True)
        return Response(serializer.data)

    # list cage filtered by count_rabbits
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        message = "No hay jaulas disponibles con ese valor de count_rabbits."

        if not queryset.exists():
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)

        return super().list(request, *args, **kwargs)

    # create cage
    @extend_schema(
        examples=[
            OpenApiExample(
                "Example Schema",
                {
                    "farm_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                },
            )
        ],
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            created_cage = serializer.instance
            return Response(
                {
                    "message": "La jaula se ha creado correctamente.",
                    "data": CageSerializer(created_cage).data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            error = serializer.errors
            error_message = "No se pudo crear la jaula. Por favor, verifica los datos proporcionados."
            return Response(
                {"message": error_message, "errors": error},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # update cage
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        for field in self.read_only_fields:
            if field in request.data:
                return Response(
                    {
                        "error": f"No puedes actualizar el campo de solo lectura <<'{field}'>>"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if serializer.is_valid():
            self.perform_update(serializer)
            update_cage = self.get_object()
            return Response(
                {
                    "message": "La jaula se ha actualizado correctamente.",
                    "data": CageSerializer(update_cage).data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            error = serializer.errors
            error_message = "No se pudo actualizar la jaula. Por favor, verifica los datos proporcionados."
            return Response(
                {"message": error_message, "errors": error},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # delete cage
    def destroy(self, request, pk=None):
        cage = self.serializer_class.Meta.model.objects.filter(id=pk, is_active=True).first()
        if cage:
            cage.is_active = False
            cage.save()
            return Response(
                {"message": "Jaula eliminada correctamente"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"message": "La jaula no existe o ya fue eliminada"},
                status=status.HTTP_404_NOT_FOUND,
            )
            
    @extend_schema(request=CagePhotoSerializer, responses=CagePhotoSerializer)
    @action(
        detail=True, methods=["patch"], parser_classes=[MultiPartParser, FormParser]
    )
    def change_photo(self, request, pk=None):
        cage = self.get_object()
        serializer = CagePhotoSerializer(instance=cage, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

