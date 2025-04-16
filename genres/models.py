from django.db import models


class Genre(models.Model):

    objects = None
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


