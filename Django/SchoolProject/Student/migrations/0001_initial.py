# Generated by Django 4.2.6 on 2023-10-05 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('location', models.CharField(max_length=500, verbose_name='Место жительства')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('image', models.ImageField(upload_to='Student/', verbose_name='Фото')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.grade', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
