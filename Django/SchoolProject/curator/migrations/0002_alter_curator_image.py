# Generated by Django 4.2.6 on 2023-10-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curator',
            name='image',
            field=models.ImageField(upload_to='curators/', verbose_name='Фото'),
        ),
    ]
