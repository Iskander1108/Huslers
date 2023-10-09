from django.db import models
from grade.models import Grade

class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')

    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    phone = models.CharField(max_length=50, verbose_name='Телефон')

    location = models.CharField(max_length=500, verbose_name='Место жительства')

    birth_date = models.DateField(verbose_name='Дата рождения')

    image = models.ImageField(upload_to='Student/', verbose_name='Фото')

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='Класс')

    

    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"