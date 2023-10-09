from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone','get_image']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px /">')
        else:
            return 'Not image'
        


