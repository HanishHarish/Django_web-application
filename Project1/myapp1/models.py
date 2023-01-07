from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField('name',max_length=5)
    mobile=models.CharField('mobile',max_length=10)
    email=models.CharField('email',max_length=20)
    address=models.CharField('address',max_length=50)