# Generated by Django 4.1.6 on 2023-02-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0009_new_bike_reliability_alter_new_bike_veloformat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_bike',
            name='reliability',
            field=models.IntegerField(blank=True, default=0, verbose_name='Поломок на 100 шт.'),
        ),
    ]
