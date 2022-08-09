from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=10, null=True)


class Car(models.Model):
    COLOR_CHOICES = (
        ('b', 'black'),
        ('w', 'white')
    )
    name = models.CharField(max_length=10, null=True)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='b')
    price = models.IntegerField(null=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True)
