# Generated by Django 4.2.6 on 2023-10-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zauch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('image', models.ImageField(upload_to='Director/', verbose_name='Изображение')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Телефон')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Зауч',
                'verbose_name_plural': 'Заучи',
            },
        ),
    ]
