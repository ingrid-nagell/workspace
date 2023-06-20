# Get stock prices and news through APIs

import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
COMPANY_QUERY = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "4C9LIES20LWNAEG0"
NEWS_KEY = "c17e8e173c6b417081b7373b8c04fb3c"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_KEY,
}

news_params = {
    "q": COMPANY_QUERY,
    "apiKey": NEWS_KEY,
    "language": "en",
    "sortBy":"publishedAt",
}

# Datetime variables
yesterday = dt.datetime.now() - dt.timedelta(1)

# yesterday as str
d_1 = dt.datetime.strftime(yesterday, '%Y-%m-%d')

# Now minus 2 as str, controlling for weekends
if yesterday.isoweekday()==1:
    d_2 = dt.datetime.strftime(yesterday - dt.timedelta(3), '%Y-%m-%d')
elif 1 < yesterday.isoweekday() < 6:
    d_2 = dt.datetime.strftime(yesterday - dt.timedelta(1), '%Y-%m-%d')

# Get change in stock prize 
stock_r = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_r.json()

price_d_m1 = float(stock_data['Time Series (Daily)'][d_1]['4. close'])
price_d_m2 = float(stock_data['Time Series (Daily)'][d_2]['4. close'])

# 3 latest articles mentioning STOCK NAME:
news_r = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_r.json()["articles"][0:3]

def get_articles(data, stock_name):
    """Function extractiong latest articles for a given company."""
    with open(f"articles_{stock_name}", "w") as f:
        f.write(f"Latest three articles for {stock_name}.\nUpdated: {dt.datetime.now()}.")
        for n, article in enumerate(data):
            f.write(f"\n\nArticle number:{n+1}\nPublished ts: {article['publishedAt']}\nMedium: {article['source']['name']}\nTitle: {article['title']}\nURL: {article['url']}")

def check_stock(stock_name, company, new, orig, data):
    """Function checking change in stock prize and print out latest news if significant change."""
    diff = round(((new-orig)/orig)*100, 2)
    diff_abs = abs(diff)
    if diff_abs > 1:
        print(f"\n--- Difference in stock price: {diff} ---\n")
        get_articles(data, stock_name=stock_name)
        with open(f"articles_{stock_name}", "r") as f:
            print(f.read())
    else:
        print(f"No significant change in stock price for {company}")

check_stock(stock_name = STOCK_NAME, company= COMPANY_NAME, new=price_d_m1, orig=price_d_m2, data=news_data)