from django.contrib import admin
from .models import ImagesModel

@admin.register(ImagesModel)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("title","description","created_at")
    list_filter = ("category",)
    search_fields = ("title","category","is_safe")

