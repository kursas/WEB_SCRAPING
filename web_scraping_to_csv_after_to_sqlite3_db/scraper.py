#You will learn how to scrape multiple web pages using BeautifulSoup and export the results to a CSV file using Pandas Library.
#We use books.toscrape.com as the web scraping playground and get access to the alt attribute of the images and the name of the classes.
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
books = []
for i in range(1, 5):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        starTag = article.find('p')
        star = starTag['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, star, price])

df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])
df.to_csv('AAAbooks.csv')

#output
Process finished with exit code 0
