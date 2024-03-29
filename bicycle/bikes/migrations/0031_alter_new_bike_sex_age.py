# Generated by Django 4.1.6 on 2023-02-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0030_alter_new_bike_sex_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_bike',
            name='sex_age',
            field=models.CharField(choices=[('Взрослый/мужской', 'Взрослый/мужской'), ('Детский/мужской', 'Детский/мужской'), ('Детский/мужской', 'Взрослый/женский'), ('Детский/женский', 'Детский/женский')], default='Взрослый/мужской', max_length=16, verbose_name='Пол и возраст'),
        ),
    ]
