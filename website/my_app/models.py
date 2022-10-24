from django.db import models

# Create your models here.
class User(models.Model):
    FirstName=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Username= models.CharField(max_length=30)
    user_mail=models.EmailField()


