# Generated by Django 4.1.6 on 2023-02-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0022_alter_extension_extension'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extension',
            options={'verbose_name': 'расширение', 'verbose_name_plural': 'Расширения'},
        ),
        migrations.AlterField(
            model_name='extension',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание расширения'),
        ),
        migrations.AlterField(
            model_name='new_bike',
            name='extensions',
            field=models.ManyToManyField(blank=True, to='bikes.extension'),
        ),
        migrations.AlterField(
            model_name='new_bike',
            name='model',
            field=models.CharField(max_length=30, verbose_name='Модель'),
        ),
    ]
