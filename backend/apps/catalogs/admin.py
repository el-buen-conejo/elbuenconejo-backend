from django.contrib import admin
from apps.catalogs.models import State, City, Breed


class StateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state",
    )
    search_fields = ("state",)
    ordering = ("state",)


class CityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state",
        "city",
    )
    search_fields = ("state", "city")
    ordering = ("state",)


class BreedAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "breed",
    )
    search_fields = ("breed",)
    ordering = ("breed",)


# Register your models here.
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Breed, BreedAdmin)
