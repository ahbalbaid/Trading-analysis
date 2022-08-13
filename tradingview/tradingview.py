from tradingview_ta import TA_Handler, Interval, Exchange
import pandas
df = pandas.read_csv('Tickers list.csv')

# Ticker('TSLA')
def Ticker(ticker):
    tick = TA_Handler(
        symbol=ticker,
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_DAY,)
    return tick


if __name__ == '__main__':

    strong = {'tickers': [], 'rec': []}
    buy = {'tickers': [], 'rec': []}

    for i in df['Symbol']:
        try:
            # STRONG_BUY
            if Ticker(i).get_analysis().summary['RECOMMENDATION'] == 'STRONG_BUY':
                strong['tickers'].append(i)
                strong['rec'].append(Ticker(i).get_analysis().summary['BUY'])
            elif Ticker(i).get_analysis().summary['RECOMMENDATION'] == 'BUY':
                buy['tickers'].append(i)
                buy['rec'].append(Ticker(i).get_analysis().summary['BUY'])
        except:
            pass

    write_strong = pandas.DataFrame(strong)
    write_strong.to_csv('strong.csv', encoding='utf-8')

    write_buy = pandas.DataFrame(buy)
    write_buy.to_csv('buy.csv', encoding='utf-8')
