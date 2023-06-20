
import requests
import datetime as dt

PATH = "C:\\Users\\G020772\\repos\\workspace\\gjensidige_stocks_app"

STOCK_NAME = "GJNSF"
COMPANY_NAME = "GJENSIDIGE FORSIKRING ASA"
COMPANY_QUERY = "Gjensidige AND forsikring"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

VAR_PATH = "C:\\Users\\G020772\\repos\\secrets.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)

STOCK_KEY = keys["STOCK_KEY"]
NEWS_KEY = keys["NEWS_KEY"]

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_KEY,
}

news_params = {
    "q": COMPANY_QUERY,
    "apiKey": NEWS_KEY,
    "language": "no",
    "sortBy":"publishedAt",
}

stock_r = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_r.json()

news_r = requests.get(NEWS_ENDPOINT, params=news_params)
results = news_r.json()["totalResults"]
gjensidige_data = news_r.json()["articles"][0:10]
print("\n--- Total results:", results, "---\n\n")

def get_articles(data, stock_name):
    """Function extracting latest articles for company."""
    with open(f"{PATH}\\articles_{stock_name}", "w") as f:
        f.write(f"Latest articles for {stock_name}.\nUpdated: {dt.datetime.now()}.")
        for n, article in enumerate(data):
            f.write(f"\n\nArticle number:{n+1}\nPublished ts: {article['publishedAt']}\nMedium: {article['source']['name']}\nTitle: {article['title']}\nURL: {article['url']}")

get_articles(gjensidige_data, STOCK_NAME)