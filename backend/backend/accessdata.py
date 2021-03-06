
import grequests
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt 
import csv 
import pandas as pd
import json
from stock.models import Stock







get_url= 'http://push2.eastmoney.com/api/qt/stock/get?fields=f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f57,f58,f71,f116,f117,f60,f162,f163,f164,f167,f168,f170,f173&secid=' 


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


@csrf_exempt
def accessdata(request):
    LIST = json.loads(request.body)
    b = accessformat(LIST)
    print(b)
    #print(stocknowdata)
    return HttpResponse(json.dumps(b))





def accessformat(LIST):
    stocknowdata = LIST['data2']['data']
    if(stocknowdata ==None):
        return 'None'
    listnow = list(stocknowdata.values())
    listnew = [listnow[10],listnow[11],listnow[0],listnow[1],
                listnow[21],listnow[2],listnow[3],listnow[12],
                listnow[8],listnow[9],listnow[4],listnow[5],
                listnow[6],listnow[7],listnow[13],listnow[14],
                listnow[15],listnow[16],listnow[17],listnow[18],
                listnow[12],listnow[20],listnow[22]]
    #print(listnew)
    label = ['股票代码','股票名称','最新价','最高价','涨跌幅','最低价','开盘价','昨收',
                '涨停','跌停','成交量(手)','成交额','外盘','量比','均价',
                '总市值','流通市值','市盈(动)','静市盈率','滚动市盈率','市净率',
                '换手率','ROE']
    #df = pd.DataFrame(columns=label)
    b=dict(zip(label,listnew))
    return b



def get_code(stockcode):
    QuerySet = Stock.objects.filter(content = stockcode)
    if(len(QuerySet)==0):
        return False
    else:
        return "1."+stockcode

@csrf_exempt
def get_allcode(request):
    QuerySet = Stock.objects.all()
    list =[]
    dictlist = []
    stockdict = {}
    for stock in QuerySet:
        list.append(get_url+"1."+stock.content)
    #print(list)
    tasks = [grequests.get(u) for u in list]
    datalist = grequests.map(tasks,size= 2000)
    for data in datalist:
        dict ={'data2':json.loads(data.text)}
        dictlist.append(accessformat(dict))
    for i in range(len(dictlist)):
        stockdict[i] = dictlist[i]

    #print(stockdict)
    return HttpResponse(json.dumps(stockdict))

def url_request(url,stockcode):
    httpsession = requests.session()
    try:
        r = httpsession.get(url+stockcode)
        r.raise_for_status()
        r.encoding = "UTF-8"
        return r.text
    except:
        return '产生异常'




