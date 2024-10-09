from django.db import models
from datetime import datetime
from author.models import Author

class Blogs(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title
