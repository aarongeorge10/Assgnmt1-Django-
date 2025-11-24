from django.db import models

# Create your models here.
class crud(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

