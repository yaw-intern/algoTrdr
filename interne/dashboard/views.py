from django.shortcuts import render
from datetime import datetime
import json
from decimal import Decimal, ROUND_UP
from django.http import HttpResponse
import yfinance as yf
import pandas as pd
# Create your views here.
def dashboard(request):
    tesla = yf.Ticker('TSLA')
    ticka = tesla.info['shortName']
    teslaData = tesla.history(period="5d")['Close']
    teslaData = pd.DataFrame(teslaData)
    dJSON = teslaData.to_json(orient="columns")
    #print(dJSON)
    aList = json.loads(dJSON)
    dateList = []
    priceList = []
    keyOnly = aList['Close'].keys()
    priceOnly =aList['Close'].values()

    stocks = ['GBPUSD=X', 'TSLA'] 
    stockNames = []

    for stock in stocks:
        info = yf.Ticker(stock).info['shortName']
        stockNames.append(info)

    for value in priceOnly:
        priceList.append(value)
        
    for key in keyOnly:
       
        key = datetime.fromtimestamp(5).strftime("%B")
        dateList.append(key)

     
    priceList = []
    for stock in stocks:
        temp = yf.Ticker(stock)
        price = temp.history(rounding=True)['Close'].iloc[-1]
        priceList.append(price)
    tickerList = []
    for ticker in stocks:
        temp = yf.Ticker(ticker).info['shortName']
        tickerList.append(temp)

    mylist = zip(tickerList, priceList)
    
    print(priceList)
   #data = df.to_json()[1:-1].replace('},{', '} {')
    ctx ={
        "mylist": mylist
    }
   
    return render(request, 'dashboard.html', ctx)

