from django.db import models
from django.contrib.auth.models import User


class Rubric(models.Model):

    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bb(models.Model):
    list_display = ('title', 'content', 'price', 'published', 'rubric')

    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")

    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявение"
        ordering = ['-published']
