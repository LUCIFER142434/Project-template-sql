from django.db import models

class User(models.Model):
    name = models.CharField(max_length=24)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
