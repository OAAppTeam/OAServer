__author__ = 'Justin'

from django.db import models
from django.contrib import admin

class TestModel(models.Model):
    name = models.CharField(max_length=5)

admin.site.register(TestModel)