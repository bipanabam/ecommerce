from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy('email address'),unique=True)
    address = models.CharField(max_length=256,blank=True)
    phone_no = models.PositiveIntegerField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email