from django.db import models
from django.core.validators import MaxValueValidator


class Book(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    date = models.DateField()
    ISBN = models.IntegerField(validators=[MaxValueValidator(9999999999999)])

    def __str__(self):
        return f'{self.name}'
