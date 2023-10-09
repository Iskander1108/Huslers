from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['number', 'char', 'curator']
    list_filter = ['curator']
    search_fields = ['number', 'char']
    


# Register your models here.
