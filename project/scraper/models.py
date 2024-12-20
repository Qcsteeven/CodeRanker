from django.db import models

class Book(models.Model):
    lang = models.CharField(max_length=255, blank=True, default='ЯП')
    title = models.CharField(max_length=255, blank=True, default='Нет названия')
    author = models.CharField(max_length=255, blank=True, default='Нет автора')
    ref = models.CharField(max_length=50, blank=True, default='Нет ссылки')

    def __str__(self):
        return self.title

class Language(models.Model):
    ind = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=50)
    change = models.CharField(max_length=50)

    def __str__(self):
        return self.name
