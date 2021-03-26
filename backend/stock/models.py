from django.db import models
import csv
# Create your models here.
class Stock(models.Model):
    title = models.CharField(max_length=50)
    content =models.CharField(max_length=500)
    #t_new  = models.DecimalField()
   # t_high = models.DecimalField()
    #t_low = models.DecimalField()
   # t_open = models.DecimalField()
    class Meta:
        db_table = 't_stock'


    



