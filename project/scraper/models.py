from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, blank=True, default='Нет названия')
    author = models.CharField(max_length=255, blank=True, default='Нет автора')
    price = models.CharField(max_length=50, blank=True, default='Нет цены')

    def __str__(self):
        return self.title

class Language(models.Model):
    ind = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=50)
    change = models.CharField(max_length=50)

    def __str__(self):
        return self.name
