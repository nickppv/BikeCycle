# Generated by Django 4.1.6 on 2023-02-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0005_new_bikes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_bikes',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='new_bikes',
            name='sex_age',
            field=models.CharField(default='Взрослый', max_length=10),
        ),
        migrations.AlterField(
            model_name='new_bikes',
            name='veloformat',
            field=models.CharField(default='Горный', max_length=15),
        ),
    ]
