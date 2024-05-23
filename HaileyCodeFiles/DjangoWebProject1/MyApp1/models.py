from django.db import models

# Create your models here.
class teacher(models.Model):
    Names = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)    


class assets(models.Model):
    type = models.CharField(max_length=32)
    teacher = models.CharField(max_length=32)
