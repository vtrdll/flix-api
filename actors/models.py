from django.db import models


NATIONALITY_CHOICES = (
    ('AFEGANISTÃO', 'Afghanistan'),
    ('ALEMANHA', 'Germany'),
    ('ARGENTINA', 'Argentina'),
    ('AUSTRÁLIA', 'Australia'),
    ('ÁUSTRIA', 'Austria'),

)


class Actor (models.Model):

    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
