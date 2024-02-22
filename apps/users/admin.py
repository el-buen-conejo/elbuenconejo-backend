from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "is_producer",
        "username",
        "email",
        "is_active",
        "created",
        "updated",
    )
    search_fields = ("username", "email", "is_producer")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
