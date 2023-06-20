from datetime import datetime

class PriceAlert():
    def __init__(self, current_price, price_threshold, product, shopping_url):
        self.current_price = current_price
        self.price_threshold = price_threshold
        self.product = product
        self.shopping_url = shopping_url

    def check_price(self):
        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        if self.current_price < self.price_threshold:
            savings = self.price_threshold - self.current_price
            print(
                f"""
--------------------
{now}

The current price is {self.current_price}. You save {savings} NOK if you buy the {self.product} now. 
                
Go to {self.shopping_url}.
--------------------
"""
            )
        else:
            print(f"""
--------------------
{now}

The current price is {self.current_price} NOK. It is not below the threshold of {self.price_threshold} NOK.
--------------------
"""
            )