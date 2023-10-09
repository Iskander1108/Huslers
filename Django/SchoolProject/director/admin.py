from django.contrib import admin
from .models import Director
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'first_name', 'last_name', 'phone', 'birth_date']
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['birth_date']
    empty_value_display = '-пусто-' 


    def  get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="100" height="100"')
        else:
            return mark_safe('нет картинки')
        


