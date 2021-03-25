from django.shortcuts import render
from rest_framework import viewsets
import csv
# Create your views here.
from .models import Stock
from .serials import StockSerializer

import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))             # 定位到django根目录
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")   # django的settings文件
django.setup()




class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


    def write(self):
        with open('D:\\股票数据\\stocklist.csv','r',encoding='utf-8') as f:
            reader = csv.reader(f)
            csv_list = []
            for row in reader:
                if tuple([row[0]]) not in csv_list:
                    csv_list.append(row[0])
            Stock.objects.bulk_create(csv_list)

    