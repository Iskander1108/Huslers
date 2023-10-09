from django.db import models
from curator.models import Curator



# Create your models here.
class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100, verbose_name='Урок')
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE, verbose_name='Куратор')

    def __str__(self):
        return f"Урок: {self.lesson_name}"
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'