from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField('title', max_length=330)
    body = models.TextField()
    image = models.ImageField('rasim', upload_to='poster/',)