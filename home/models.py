from django.db import models

# class User(models.Model):
#     first_name = models.CharField('Имя', max_length=30)
#     last_name = models.CharField('Фамилия', max_length=30)
class Car(models.Model):
    car_name = models.CharField('Марка машины', max_length=30)
    car_image = models.ImageField()