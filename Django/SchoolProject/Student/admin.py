from django.contrib import admin
from .models import Student
from django.utils.safestring import mark_safe

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'first_name', 'last_name', 'phone', 'location', 'birth_date', 'grade' ]
    list_filter = [ 'birth_date' ,'grade']
    search_fields = ['first_name', 'last_name', 'phone', 'location' ]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
            f"<img src='{obj.image.url}' width='400' heigth='400'>")
        else:
            return "Изображение отсутствует"
# Register your models here.
