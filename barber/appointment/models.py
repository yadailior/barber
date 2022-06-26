from django.db import models
import datetime
import calendar

# Create your models here.


class Date(models.Model):
    year=models.IntegerField()
    month=models.IntegerField()
    day=models.IntegerField()
    date=models.DateField()

