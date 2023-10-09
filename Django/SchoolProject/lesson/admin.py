from django.contrib import admin
from lesson.models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['lesson_name', 'curator']
    list_filter = ['curator']
    search_fields = ['lesson_name']
    

# Register your models here.
