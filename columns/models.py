from django.db import models

# Create your models here.
class MyModel(models.Model):
    first_field = models.CharField(max_length=50)
    second_field = models.CharField(max_length=50)
