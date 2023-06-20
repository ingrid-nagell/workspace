from bs4 import BeautifulSoup

with open("C:/Users/G020772/repos/workspace/python_bootcamp/boot45_web_scraping/website.html", encoding="utf8") as w:
    contents = w.read()

soup = BeautifulSoup(contents, 'html.parser')

# pretty indentation, structure of content:
# print(soup.prettify())

# string inside title:
# print(soup.title.string)

# get first paragraph:
# print(soup.p)

# get all paragrapghs:
all_p = soup.find_all(name = "p")
print(all_p)

for tag in all_p:
    print("----")
    print(tag.getText())

# get a specific element
author = soup.find(id="name").getText()
print("----", author)

# class is a reserved keyword in python, to search for a html class, use class_


import requests

# response = requests.get()
# movies_web_page = response.text

upvotes = [22, 1, 75, 33, 75]
links = ["abc.com", "google.com", "yolo.no", "helloworld.org", "yehee.no"]

top_votes = []

for e in range(0, 3):
    max_value = max(upvotes)
    i = upvotes.index(max_value)
    link = links[i]
    top_votes.append([link, max_value])
    upvotes.pop(i)
    links.pop(i)

print(top_votes)

    
