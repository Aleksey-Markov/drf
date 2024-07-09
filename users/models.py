from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='аватар', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='страна', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        