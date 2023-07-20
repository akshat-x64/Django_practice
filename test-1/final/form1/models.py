from django.db import models

# Create your models here.
class form1(models.Model):
    name1 = models.CharField(max_length=50) 
    eamil1 = models.CharField(max_length=50) 
    phone1 = models.CharField(max_length=10)
    website1 = models.CharField(max_length=50)
    message1 = models.TextField()
