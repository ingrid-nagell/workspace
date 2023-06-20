import requests
from bs4 import BeautifulSoup

class GetProductInfo():
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers
    
    def get_response(self):
        response = requests.get(self.url, self.headers)
        if response.status_code == 200:
            print("Successful request.")
            return response.text
        else:
            print(response.raise_for_status)
            exit()
    
    def make_soup(self):
        soup = BeautifulSoup(self.get_response(), 'lxml')
        return soup
    
    def get_product(self):
        title = self.make_soup().title.getText()
        product = title.split("|")[0].strip()
        return product
    
    def get_price(self):
        price = self.make_soup().find(class_="q as av").getText().split(",")[0].replace(chr(160), "") # what looks like white space is a unicoded value with character value of 160
        return float(price)
    
    def get_info(self):
        soup = self.make_soup()
        product = soup.title.getText().split("|")[0]
        price = float(soup.find(class_="q as av").getText().split(",")[0].replace(chr(160), ""))
        return {"product": product, "price": price}
    

# find character values:
# for l in price:
#     print(ord(l))
