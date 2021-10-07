from django.db import models


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
