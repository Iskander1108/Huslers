from typing import Any
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Тег"
        verbose_name_plural = "Теги"


        


class Post(models.Model):
    image = models.ImageField(upload_to="post/", verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name="Называние")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")  
    tag = models.ManyToManyField(Tag, verbose_name="Тег")  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
        verbose_name="Категория")
    discription = models.TextField(max_length=600, verbose_name="Описание", blank=True, null=True)
    location = models.CharField(max_length=200, verbose_name="Местоположение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return f"{self.id} | {self.title}"
    

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="ПОСТ")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    content = models.TextField(max_length=1000, verbose_name="КОНТЕНТ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.id} | {self.author} | {self.content}"





# Create your models here.

# class News(models.Model):
#     title = models.CharField(max_length=150, verbose_name="Название",
#         help_text="Название (не более 150 символов)")
    
#     description = models.TextField(max_length=600, verbose_name="Описание",
#         help_text="Напишите описание к новости")
    
#     # date = models.DateTimeField(auto_now_add=True)

#     data = models.DateField(verbose_name="Дата", 
#         help_text="Дата (необходимо указать дату)")
    
#     time = models.TimeField(verbose_name="Время", 
#         help_text="Время (необходимо указать время)")
    
#     slug = models.SlugField(max_length=200, unique=True )

#     read = models.BooleanField(default=False, verbose_name="Статус прочтения")


#     def __str__(self):
#         return f"{self.title} - Описание:\
#               {self.description[:21]}... {self.data} {self.time} -- {self.slug}"

   
# class Comments(models.Model):
#     post = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость")
#     comment = models.TextField(max_length=700, verbose_name="Комментарий", 
#         help_text="Напишите комментарии(не более 700 символов)")
    
#     created_at = models.DateTimeField(auto_now_add=True)
    

#     def __str__(self):
#         return f"{self.comment[:20]}... | Время {self.created_at}"