from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='course/photo', verbose_name='Превью курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lessons.photo', verbose_name='Превью урока', **NULLABLE)
    link = models.URLField(verbose_name='ссылка на урок', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE, related_name='course')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'Урок: {self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название подписки')
    description = models.TextField(verbose_name='Описание подписки', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
