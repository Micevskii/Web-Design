from django.db import models
from datetime import datetime

class Restaurants(models.Model):
    title = models.CharField(max_length=200)
    adress = models.CharField(max_length=100)
    small_description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)
    place = models.CharField(max_length=100, default='Gevgelija')
    def __str__(self):
        return self.title
