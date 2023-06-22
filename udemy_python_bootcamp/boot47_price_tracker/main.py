from price_alert import PriceAlert

url = "https://www.fjellsport.no/turutstyr/klatreutstyr/sikringer/kamkiler/black-diamond-camalot-ultralight-4"
headers = {"Accept-Language":"nb-NO", "sec-ch-ua":"Google Chrome"}

max_price = 1300.0

alert = PriceAlert(price_threshold = max_price, shopping_url = url, headers=headers)
alert.check_price()