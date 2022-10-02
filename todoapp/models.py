from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Todo(models.Model):

    name = models.CharField(max_length=300)
    status = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

class AddTask(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=1000)
    priority = models.CharField(max_length=10)