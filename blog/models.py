from django.db import models

class BlogModel(models.Model):
    userid=models.CharField(default='',max_length=100)
    title=models.CharField(default='',max_length=100)
    message=models.CharField(default='',max_length=100)
    







# Create your models here.
