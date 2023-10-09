from django.contrib import admin

from .models import Curator
from django.utils.safestring import mark_safe





# Register your models here.
@admin.register(Curator)
class CuratorAdmin(admin.ModelAdmin):
        list_display = ["get_image", "first_name",
        "last_name", "phone", "birth_date", "location"]
    
        list_filter = ["birth_date"]

        search_fields = ["first_name", "last_name", "phone", "location"]

        def get_image(self, obj):
            if obj.image:
                return mark_safe(
                f"<img src='{obj.image.url}' width='400' heigth='400'>")
            else:
                return "Изображение отсутствует"