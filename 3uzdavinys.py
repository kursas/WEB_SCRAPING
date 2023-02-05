#Parašyti programą kuri iš puslapio https://shop.telia.lt/telefonai/?filter=brand:samsung' rastų pigiausią ir brangiausią 
#telefono modelį
# -*- coding:utf-8 -*-
import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

with open("telia_telefonai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['PAVADINIMAS', 'MĖNESIO KAINA', 'KAINA'])
    blokai = soup.find_all('div', class_='mobiles-product-card card card__product card--anim js-product-compare-product')
    for blokas in blokai:
        pavadinimas = blokas.find('a', class_="mobiles-product-card__title js-open-product").get_text().strip()
        men_kaina = blokas.find('div', class_="mobiles-product-card__price-marker").get_text().strip()
        kaina = blokas.find_all('div', class_='mobiles-product-card__price-marker')[1].get_text().strip()
        csv_writer.writerow([pavadinimas, men_kaina, kaina])
        print(pavadinimas, men_kaina, kaina)
        
   #output
   
   Samsung Galaxy S22 20,80 €/mėn. 499 €
Samsung Galaxy Flip4 5G 24,96 €/mėn. 599 €
Samsung Galaxy S22 Ultra 39,55 €/mėn. 949 €
Samsung Galaxy A23 5G 6,21 €/mėn. 149 €
Samsung Galaxy A53 5G 11,21 €/mėn. 269 €
Samsung Galaxy S22+ 34,96 €/mėn. 839 €
Samsung Galaxy Fold4 5G 63,30 €/mėn. 1 519 €
Samsung Galaxy S21 FE 20,80 €/mėn. 499 €
Samsung Galaxy A33 12,46 €/mėn. 299 €
Samsung Galaxy Xcover6 Pro 25,38 €/mėn. 609 €
Samsung Galaxy A13 5G 7,88 €/mėn. 189 €
Samsung Galaxy A13 (A137) 128GB 8,30 €/mėn. 199 €
Samsung Galaxy XCover 5 10,38 €/mėn. 249 €
Samsung Galaxy S21 Ultra 49,55 €/mėn. 1 189 €
Samsung Galaxy Fold3 5G 41,63 €/mėn. 999 €
Samsung Galaxy S21 29,13 €/mėn. 699 €
Samsung Galaxy S20 FE 5G 20,80 €/mėn. 499 €
Samsung Galaxy A13 (A137) 32GB 6,63 €/mėn. 159 €

Process finished with exit code 0
