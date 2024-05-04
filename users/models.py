from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
