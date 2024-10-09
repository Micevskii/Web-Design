from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Gallery(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

class Image(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

from django.utils.translation import gettext_lazy as _
