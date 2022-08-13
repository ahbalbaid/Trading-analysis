from tradingview_ta import TA_Handler, Interval, Exchange
import pandas
from tradingview import Ticker
strong = pandas.read_csv('strong.csv')

sell = {'tickers':[],'rec':[]}
for i in strong['tickers']:
    sell['tickers'].append(i)
    sell['rec'].append(Ticker(i).get_analysis().summary['SELL'])


write_sell_strong = pandas.DataFrame(sell)
write_sell_strong.to_csv('strongsell.csv', encoding='utf-8')
