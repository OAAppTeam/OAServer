__author__ = 'Justin'

from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name