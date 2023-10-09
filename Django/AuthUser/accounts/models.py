# Абстрактный юзер

from typing import Any
from django.db import models
from django.contrib.auth.models import User
from .utils import validate_phone


# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/', 
            width_field="image_width" , height_field="image_height")

    image_width = models.PositiveIntegerField(
        editable=True, null=True, blank=True,
        help_text="Ширина загруженного изображения"
    )

    image_height = models.PositiveIntegerField(
        editable=True, null=True, blank=True,
        help_text="Высота загруженного изображения"
    ) 

    phone = models.CharField(max_length=20, unique=True, validators=[validate_phone])

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

