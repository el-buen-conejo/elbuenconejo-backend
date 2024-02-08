from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "first_name",
        "last_name",
        "address_id",
        "photo",
        "qualification",
        "saw_tutorial",
    )
    search_fields = (
        "first_name",
        "last_name",
    )
    ordering = ("user_id",)


admin.site.register(Profile, ProfileAdmin)
