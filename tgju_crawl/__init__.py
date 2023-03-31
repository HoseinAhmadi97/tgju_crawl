# import packages
import requests
import pandas as pd
import datetime
import calendar
import jdatetime
from bs4 import BeautifulSoup
from lxml import etree

# main functions
def get_main_symbols():
    """
        symbols in main page
    """
    
    url = 'https://www.tgju.org'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    dom = etree.HTML(str(soup))
    href = (dom.xpath('//div[@class = "nav-links"]/div[2]/ul/li/div/div/ul/li/ul/li/a/@href'))
    symbol_Fa = (dom.xpath('//div[@class = "nav-links"]/div[2]/ul/li/div/div/ul/li/ul/li/a//text()'))
    df = pd.DataFrame({'href': href, 'symbol_Fa': symbol_Fa})
    df['count_profile'] = df['href'].apply(lambda x: x.count('profile'))
    df = df.drop_duplicates(subset = 'symbol_Fa')
    df = df[df['count_profile'] == 1].drop('count_profile', axis=1).set_index('symbol_Fa')
    df['symbol_En'] = df['href'].apply(lambda x: x.split('/')[-1])
    df.loc['طلای دست دوم']['symbol_En'] = 'gold_mini_size'
    df['SYMBOL'] = df['symbol_En'].apply(lambda x: x.upper()) 
    df = df.drop('href', axis=1).drop_duplicates()
    return df
    
def get_energy_symbols():
    """
       symbols in energy page 
    """
    
    url = 'https://www.tgju.org/energy'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    dom = etree.HTML(str(soup))
    symbol_Fa = dom.xpath('//table[contains(@class,"market-table")]/tbody/tr/th/span/following-sibling::text()')
    href = dom.xpath('//table[contains(@class,"market-table")]/tbody/tr/@onclick')
    df = pd.DataFrame({'symbol_Fa': symbol_Fa, 'href': href})
    df['symbol_En'] = df['href'].apply(lambda x: x.split('/')[-1][:-1])
    df['SYMBOL'] = df['symbol_En'].apply(lambda x: x.upper())
    df = df.drop_duplicates().drop(['href'], axis=1).set_index('symbol_Fa')
    return df
    

def get_df_of_symbols():
    df = pd.concat([get_main_symbols(), get_energy_symbols()], axis=0)
    return df.drop_duplicates()

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