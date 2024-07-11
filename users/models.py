from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Lesson, Course
NULLABLE = {"blank": True, "null": True}


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


class Payments(models.Model):
    user = models.ForeignKey(User, related_name='user', verbose_name='пользователь', on_delete=models.CASCADE)
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    payed_lesson = models.ForeignKey(Lesson, related_name='lessons', verbose_name='урок', on_delete=models.CASCADE, **NULLABLE)
    payed_course = models.ForeignKey(Course, related_name='payed_course', verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_type = models.CharField(max_length=20, verbose_name='способ оплаты')

    def __str__(self):
        if self.payed_lesson:
            return f'Оплата пользователем {self.user} за урок {self.payed_lesson}'
        return f'Оплата пользователем {self.user} за курс {self.payed_course}'