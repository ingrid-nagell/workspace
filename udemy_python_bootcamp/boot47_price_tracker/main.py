from extract_website_content import GetProductInfo
from price_alert import PriceAlert

url = "https://www.fjellsport.no/turutstyr/klatreutstyr/sikringer/kamkiler/black-diamond-camalot-ultralight-4"
headers = {"Accept-Language":"nb-NO", "sec-ch-ua":"Google Chrome"}

max_price = 1300.0

gpi = GetProductInfo(url, headers)
info = gpi.get_info()

alert = PriceAlert(info['price'], max_price, info["product"], url)
alert.check_price()