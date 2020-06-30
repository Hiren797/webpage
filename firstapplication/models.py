from django.db import models
class Userdetails(models.Model):
    userid=models.CharField(max_length=5)
    username=models.CharField(max_length=20)
    usercontact=models.CharField(max_length=10)
    useraddress=models.CharField(max_length=100)

# Create your models here.
