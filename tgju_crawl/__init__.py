# import packages
import requests
import pandas as pd
import datetime
import calendar
import jdatetime
from bs4 import BeautifulSoup
from lxml import etree

# main function
def get_df_of_symbols(url = 'https://www.tgju.org/local-markets'):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    dom = etree.HTML(str(soup))
    row = dom.xpath('//table/tbody/tr/th/text()')
    symbol = dom.xpath('//table/tbody/tr/@data-market-row')
    df = (pd.DataFrame({'type': row, 'symbol': symbol})[:-11]).set_index('type')
    df['SYMBOL'] = df['symbol'].apply(lambda x: x.upper()) 
    return df

def get_tgju_data(symbol):
    # get symbols
    df_of_symbols = get_df_of_symbols()
    SYMBOL = df_of_symbols.loc[symbol]['SYMBOL']
    # get data
    r = requests.get(f'https://platform.tgju.org/fa/tvdata/history?symbol={SYMBOL}')
    df_data = r.json()
    df_data = pd.DataFrame({'Date':df_data['t'],'Open':df_data['o'],'High':df_data['h'],'Low':df_data['l'],'Close':df_data['c'],})
    df_data['Date'] = df_data['Date'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df_data = df_data.set_index('Date')
    df_data.index = df_data.index.to_period("D")
    df_data.index=df_data.index.to_series().astype(str)
    df_data = df_data.reset_index()
    df_data['Symbol'] = symbol
    df_data['Date'] = pd.to_datetime(df_data['Date'])
    df_data['Weekday']=df_data['Date'].dt.weekday
    df_data['Weekday'] = df_data['Weekday'].apply(lambda x: calendar.day_name[x])
    df_data['J-Date']=df_data['Date'].apply(lambda x: str(jdatetime.date.fromgregorian(date=x.date())))
    df_data = df_data.set_index('J-Date')
    df_data=df_data[['Date','Weekday','Open','High','Low','Close', 'Symbol']]
    return df_data