from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "address",
        "state",
        "city",
    )
    search_fields = (
        "state",
        "city",
    )
    ordering = ("city",)


admin.site.register(Address, AddressAdmin)
