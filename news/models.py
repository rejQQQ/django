from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField('Дата', default=timezone.now)  # добавлено поле для даты

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Софт'
        verbose_name_plural = 'Софты'
