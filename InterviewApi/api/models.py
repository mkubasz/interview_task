from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=4, unique=True)
    value = models.TextField()
