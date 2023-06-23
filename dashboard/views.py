from django.shortcuts import render, redirect
from datetime import datetime
import json
from decimal import Decimal, ROUND_UP
from django.http import HttpResponse
import yfinance as yf
import pandas as pd
from .forms import findUserForm
from django.contrib.auth.models import User
# Create your views here.



def dashboard(request):
    if request.user.is_authenticated:
        
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

        stocks = ['GBPUSD=X', 'TSLA', 'AAPL'] 
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
        
        
        if request.method=="POST":
            form = findUserForm(request.POST)
            username = request.POST['usrname']
            print("Username is ", username)
            if User.objects.filter(username=username).exists():
                print("Hooray!")
                result= User.objects.get(username=username)
            else:
                print("No record")
                result = None
                
        else:
            result = None
            form = findUserForm()
    
        ctx ={
            "mylist": mylist,
            "form": form,
            "result": result,
            "currentUser": request.user.username,
        }
        
        return render(request, 'dashboard.html', ctx)
    else:
        return redirect('/login')

