# Generated by Django 4.1.6 on 2023-02-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0006_alter_new_bikes_description_alter_new_bikes_sex_age_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New_Bikes',
            new_name='New_Bike',
        ),
    ]