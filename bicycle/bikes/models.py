from django.db import models


class New_Bikes(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    sex_age = models.CharField(max_length=10)
    veloformat = models.CharField(max_length=15)
    picture = models.TextField()
    price = models.FloatField()
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.brand} - {self.model}'


class Sportsmens(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    distance = models.IntegerField()
    count_trophy = models.IntegerField
