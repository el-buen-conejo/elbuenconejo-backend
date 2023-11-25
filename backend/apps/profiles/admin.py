from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "is_producer",
        "first_name",
        "last_name",
        "address_id",
        "photo",
    )
    search_fields = (
        "first_name",
        "last_name",
    )
    ordering = ("is_producer",)


admin.site.register(Profile, ProfileAdmin)
