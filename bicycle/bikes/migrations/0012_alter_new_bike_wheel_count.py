# Generated by Django 4.1.6 on 2023-02-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0011_new_bike_wheel_count_alter_new_bike_veloformat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_bike',
            name='wheel_count',
            field=models.CharField(choices=[('UNI', 'Уницикл'), ('BI', 'Обычный'), ('TRI', 'Трицикл'), ('OTH', 'Другое')], default='BI', max_length=3, verbose_name='Кол-во колес'),
        ),
    ]
