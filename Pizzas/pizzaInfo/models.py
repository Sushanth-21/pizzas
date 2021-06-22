from django.db import models
from django.contrib.auth.models import User


class Toppings(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=7)
    size = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return self.size+"-"+self.type+" Pizza"
