from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from PIL import Image

User._meta.get_field('email')._unique = True

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to="images", validators=[FileExtensionValidator(['png'])])

    def __str__(self):
        return f'{self.avatar.name}'
