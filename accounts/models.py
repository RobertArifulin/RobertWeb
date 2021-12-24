from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from PIL import Image
from django.forms import TextInput, EmailInput, PasswordInput


# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to="images", validators=[FileExtensionValidator(['png'])])

    def __str__(self):
        return f'{self.avatar.name}'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": TextInput(attrs={
                'placeholder': "Введите логин",
                'class': "form-control"
            }),
            "email": EmailInput(attrs={
                'placeholder': "Введите адрес электронной почты",
                'class': "form-control"
            }),
            "password1": PasswordInput(attrs={
                'placeholder': "Введите пароль",
                'class': "form-control"
            }),
            "password2": PasswordInput(attrs={
                'placeholder': "Повторите пароль",
                'class': "form-control"
            })
        }