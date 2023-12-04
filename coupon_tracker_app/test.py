from bs4 import BeautifulSoup
import requests
import re

url = "https://www.obos.no/medlem/medlemsfordeler?view=list"

params = {"view": "list"}

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}


response = requests.get(url, headers=HEADERS)
obos = response.text

soup = BeautifulSoup(obos, 'html.parser')

# elements = soup.find_all(string=re.compile("member_event"))#["href"]
# class_="relative flex w-full gap-8 break-words p-2 no-underline"
elements = soup.find_all("a")#["href"]


print(len(elements))