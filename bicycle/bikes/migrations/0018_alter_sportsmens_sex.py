# Generated by Django 4.1.6 on 2023-02-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0017_sportsmens_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsmens',
            name='sex',
            field=models.CharField(choices=[('MEN', 'Man'), ('WOMAN', 'Woman')], default='Man', max_length=5, verbose_name='Пол'),
        ),
    ]