from django.http import HttpResponse
from django.views.decorators.csrf import  csrf_exempt 
import csv 
from stock.models import Stock
@csrf_exempt
def access_stock_code(request):
    print(request.POST.get('stockcode'))
    stockcode = request.POST.get('stockcode')
    if(get_code(stockcode)==False):
        return HttpResponse('Not Found this stock!!!')
    return HttpResponse(get_code(stockcode),'string')

'''@csrf_exempt
def write_stock_list(self):
    with open('D:\\股票数据\\stocklist.csv','r',encoding='utf-8') as f:
        reader = csv.reader(f)
        csv_list = []
        for row in reader:
            
            if tuple([row[0]]) not in csv_list:
                obj = Stock(title = row[0],content = row[1])
                csv_list.append(obj)
        Stock.objects.bulk_create(csv_list)'''


def get_code(stockcode):
    QuerySet = Stock.objects.filter(content = stockcode)
    if(len(QuerySet)==0):
        return False
    else:
        return "1."+stockcode

