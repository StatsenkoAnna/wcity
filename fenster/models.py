from django.db import models

# Create your models here.
class Fenster(models.Model):
    fenster_width = models.IntegerField()
    window_view = models.CharField(default='', max_length=1024)
