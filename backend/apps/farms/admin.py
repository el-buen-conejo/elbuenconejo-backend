from django.contrib import admin
from apps.farms.models import Farm


class FarmAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
        "is_active",
    )
    search_fields = (
        "id",
        "default",
        "name",
        "address",
        "is_active",
    )
    ordering = ("name",)
    pass


admin.site.register(Farm, FarmAdmin)

