from django.db import models
NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lessons.photo', verbose_name='Превью урока', **NULLABLE)
    link = models.URLField(verbose_name='ссылка на урок')

    def __str__(self):
        return f'Урок: {self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='course/photo', verbose_name='Превью курса', **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='Уроки курса', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
