# Generated by Django 4.1.6 on 2023-02-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0027_alter_new_bike_add_date_alter_new_bike_model_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_bike',
            name='brand_slug',
            field=models.SlugField(blank=True, verbose_name='Slug Брэнда'),
        ),
        migrations.AlterField(
            model_name='new_bike',
            name='model_slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slug Модели'),
        ),
    ]
