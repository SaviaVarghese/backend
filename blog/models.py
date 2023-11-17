from django.db import models

class BlogModel(models.Model):
    userid=models.CharField(default='',max_length=100)
    title=models.CharField(default='',max_length=100)
    message=models.CharField(default='',max_length=100)
    
class UserModel(models.Model):
    email=models.CharField(default='',max_length=100)
    password=models.CharField(default='',max_length=100)
    pic=models.CharField(default='',max_length=100)
    name=models.CharField(default='',max_length=100)
    







