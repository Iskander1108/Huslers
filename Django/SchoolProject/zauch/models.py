from django.db import models

# Create your models here.
class Zauch(models.Model):
    first_name  = models.CharField(max_length=255, verbose_name= "Имя")
    
    last_name  = models.CharField(max_length=255, verbose_name= "Фамилия")

    image = models.ImageField(upload_to='Zauchi/', verbose_name= "Изображение")

    phone = models.CharField(verbose_name= "Телефон", max_length=50, unique=True,)

    birth_date = models.DateField(verbose_name= "Дата рождения")


    def __srt__(self):
        return f"Зауч {self.first_name} {self.last_name}"
    

    class Meta:
        verbose_name = "Зауч"
        verbose_name_plural = "Заучи"
