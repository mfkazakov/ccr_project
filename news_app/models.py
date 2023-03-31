from django.db import models
from django.utils.timezone import localdate
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class News(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    text = models.TextField(null=False, verbose_name='Текст новости')
    publication_date = models.DateField(default=localdate, verbose_name='Дата новости')
    author = models.CharField(max_length=255, null=False, verbose_name='Автор новости')
    image = models.ImageField(upload_to='news/%Y-%m-%d', null=False, blank=False, verbose_name='Изображение')
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFit(200, 200)],
                                 format='PNG',
                                 options={'quality': 60})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

