from django.db import models

# Create your models here.
class Curator(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')

    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    phone = models.CharField(max_length=50, verbose_name='Телефон')

    location = models.CharField(max_length=500, verbose_name='Место жительства')

    birth_date = models.DateField(verbose_name='Дата рождения')

    image = models.ImageField(upload_to='curators/', verbose_name='Фото')
    

    def __str__(self):
        return f"Куратор: {self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"



    