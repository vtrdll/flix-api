from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movie_genre')
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movie_actor')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
