from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Edge()
options = webdriver.EdgeOptions()
options.add_argument('--headless')
products = []  # List to store name of the product
prices = []  # List to store price of the product

driver.get("https://computacion.mercadolibre.com.co/portatiles/")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.find_all('li', attrs={'class': 'ui-search-layout__item'}):
    name = a.find('h2').text
    price = a.find('span', attrs={'class': 'price-tag-fraction'}).text
    products.append(name)
    prices.append(price)
    print(name + price)

df = pd.DataFrame({'product': products, 'price': prices})
# df.to_csv('products.csv', index=False, encoding='utf-8')
df.to_json('products.json', orient='records')
