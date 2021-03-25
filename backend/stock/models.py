from django.db import models
import csv
# Create your models here.
class Stock(models.Model):
    title = models.CharField(max_length=50)
    content =models.CharField(max_length=500)
    class Meta:
        db_table = 't_stock'


