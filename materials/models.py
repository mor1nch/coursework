from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.CharField(max_length=500, verbose_name='Описание курса')
    course_topics = models.CharField(max_length=500, verbose_name='Темы курса')
    image = models.ImageField(upload_to='courses/', verbose_name='Изображение', null=True, blank=True)
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название урока', unique=True)
    image = models.ImageField(upload_to='lessons/', verbose_name='Изображение урока', null=True, blank=True)
    description = models.TextField(verbose_name='Описание урока')
    text = models.TextField(verbose_name='Информация урока')
    video = models.TextField(verbose_name='Видео урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
