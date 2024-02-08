from django.contrib import admin
from .models import Cage

class CageAdmin(admin.ModelAdmin):
    list_display = ("id", "farm_id", "count_rabbits", "price", "is_public", "is_active",)
    search_fields = ("id", "farm_id", "count_rabbits", "price", "is_public", "is_active",)
    ordering = ("price",)


admin.site.register(Cage, CageAdmin)
