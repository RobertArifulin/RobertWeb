from django.db import models
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True
# Create your models here.

class Leaderboard(models.Model):
    place = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return f'{self.place} - {self.score}'


class Background(models.Model):
    background = models.ImageField()

    def __str__(self):
        return f'{self.background.name}'
