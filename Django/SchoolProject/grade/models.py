from django.db import models
from curator.models import Curator



# Create your models here.
class Grade(models.Model):
    char = models.CharField(max_length=3, verbose_name='Буква класса')
    number = models.PositiveIntegerField(verbose_name='Номер класса')
    curator = models.ForeignKey(Curator,on_delete=models.CASCADE, verbose_name='Куратор')

    def __str__(self):
        return f"Класс: {self.char}{self.number}"
    
    class Meta: 
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


