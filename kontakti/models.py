from django.db import models
from datetime import datetime

class Contactform(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   subject = models.CharField(max_length=100)
   message = models.TextField(blank=True)
   contact_date = models.DateTimeField(default=datetime.now, blank=True)
   user_id = models.IntegerField(blank=True)
   def __str__(self):
      return self.name