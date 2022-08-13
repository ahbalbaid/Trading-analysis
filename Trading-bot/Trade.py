import sympy as sp
from math import *
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from binance.client import Client

file=open("ETH.csv",'r')
result=open("resultETH.csv",'a+')
mon={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
monthin=input("Please enter a month: ")
year=input("Please enter a year: ")
ratein=float(input("Please enter the minimum percentage of the rate of change:"))
datein=[]
datetime=[]
unix=[]
symbol=[]
open=[]
high=[]
low=[]
close=[]
volumeEHT=[]
volumeUSDT=[]
tradecount=[]
######################in the intarvel
unixin=[]
symbolin=[]
openin=[]
highin=[]
lowin=[]
closein=[]
volumeEHTin=[]
volumeUSDTin=[]
tradecountin=[]


all =list(file)
month=str(mon[monthin])

#unix,date,symbol,open,high,low,close,Volume ETH,Volume USDT,tradecount
for i in all :
    unix.append(all[all.index(i)].split(',')[0]) #adding dates from "all" to "datetime"
    datetime.append(all[all.index(i)].split(',')[1])
    symbol.append(all[all.index(i)].split(',')[2])
    open.append(all[all.index(i)].split(',')[3])
    high.append(all[all.index(i)].split(',')[4])
    low.append(all[all.index(i)].split(',')[5])
    close.append(all[all.index(i)].split(',')[6])
    volumeEHT.append(all[all.index(i)].split(',')[7])
    volumeUSDT.append(all[all.index(i)].split(',')[8])
    tradecount.append(all[all.index(i)].split(',')[9])


if month=='1' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')

elif month=='2' :
    for i in range(28):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j< 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='3' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='4' :
    for i in range(30):
        if i + 1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0' + str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='5' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='6' :
    for i in range(30):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='7' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='8' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='9' :
    for i in range(30):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='10' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='11' :
    for i in range(14):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')
elif month=='12' :
    for i in range(31):
        if i+1 < 10:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + '0'+str(i + 1)) + ' ' + f'{j}:00:00')
        else:
            for j in range(24):
                if j < 10:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'0{j}:00:00')
                else:
                    datein.append(str(year + '-' + month + '-' + str(i + 1)) + ' ' + f'{j}:00:00')

#for i in datein:
for i in datein :
    unixin.append(unix[datetime.index(i)])
    symbolin.append(symbol[datetime.index(i)])
    openin.append(open[datetime.index(i)])
    highin.append(high[datetime.index(i)])
    lowin.append(low[datetime.index(i)])
    closein.append(close[datetime.index(i)])
    volumeEHTin.append(volumeEHT[datetime.index(i)])
    volumeUSDT.append(volumeUSDT[datetime.index(i)])
    tradecount.append(tradecount[datetime.index(i)])

result.write("Rate of Change,percentage of the rate of change,From,To\n")
for i in range(len(openin)):
    O = float(openin[i])
    H = float(highin[i])
    L = float(lowin[i])
    C = float(close[i])
    T = datein[i]
    A = (O + H + L + C) / 4
    if (i+1) <len(openin):
        O2 = float(openin[i + 1])
        H2 = float(highin[i + 1])
        L2 = float(lowin[i + 1])
        C2 = float(close[i + 1])
        T2 = datein[i + 1]
        B = (O2 + H2 + L2 + C2) / 4
        if A > B:
            currentrate=round((((B-A)*(-1))/A)*100,3)
            if currentrate>=ratein:
                result.write(f"{B - A},{currentrate}%,{T},{T2}\n")

