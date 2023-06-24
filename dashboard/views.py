from django.shortcuts import render, redirect
from datetime import datetime
import json
from decimal import Decimal, ROUND_UP
from django.http import HttpResponse
import yfinance as yf
from django.contrib.auth import get_user_model
import pandas as pd
from .forms import findUserForm
from django.contrib.auth.models import User
from usr_chat.models import Message
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
        
        
        

        userid = request.user.id
        #get all message from table where recipient_id or sender id == userid && roomid IS UNIQUE
        convos = Message.objects.all()
        
    
        ctx ={
            "mylist": mylist,
            "currentUser": request.user.username,
            "convos":convos,   
        }
        if request.method=="POST":
            form = findUserForm(request.POST)
            ctx["form"] = form
            username = request.POST['usrname']
            print("Username is ", username)
            if User.objects.filter(username=username).exists():
                print("Hooray!")
                result= User.objects.get(username=username) 
                ctx["result"] = result
            else:
                print("No record")
                result = None
                
        else:
            form = findUserForm()
            ctx["form"] = form
        
        return render(request, 'dashboard.html', ctx)
    else:
        return redirect('/login')

def conversations(request):
    userid = request.user.id
    #get all message from table where recipient_id or sender id == userid && roomid IS UNIQUE
    convos = Message.objects.all()#.filter(sender_id=userid or recipient_id==userid)
   
    ctx ={
        "convos":convos,    
    }
    return render(request, 'conversations.html', ctx)