from django.db import models
from PIL import Image


# Create your models here.
class Avatar(models.Model):
    avatar = models.ImageField()

    def __str__(self):
        return f'{self.avatar.name}'
