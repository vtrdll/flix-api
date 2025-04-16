from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='review_movie')
    stars = models.IntegerField(validators=[MinValueValidator(0, 'Avaliação nao pode ser inferior a 0'),
                                            MaxValueValidator(5, 'Avaliação nao pode ser superior   a 5')])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
