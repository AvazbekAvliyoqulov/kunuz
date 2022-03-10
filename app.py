from bs4 import BeautifulSoup
import requests

def kun(uzb, jahon, iqtisod, jamiyat, fantex, sport, buscl):
    uzb = BeautifulSoup(requests.get(uzb).text, 'html.parser')
    jahon = BeautifulSoup(requests.get(jahon).text, 'html.parser')
    iqtisod = BeautifulSoup(requests.get(iqtisod).text, 'html.parser')
    jamiyat = BeautifulSoup(requests.get(jamiyat).text, 'html.parser')
    fantex = BeautifulSoup(requests.get(fantex).text, 'html.parser')
    sport = BeautifulSoup(requests.get(sport).text, 'html.parser')
    buscl = BeautifulSoup(requests.get(buscl).text, 'html.parser')
    uzb1 = uzb.find_all('a', class_='news__title')
    jahon1 = jahon.find_all('a', class_='news__title')
    iqtisod1 = iqtisod.find_all('a', class_='news__title')
    jamiyat1 = jamiyat.find_all('a', class_='news__title')
    fantex1 = fantex.find_all('a', class_='news__title')
    sport1 = sport.find_all('a', class_='news__title')
    buscl1 = buscl.find_all('a', class_='news__title')
    print("O'zbekiston va jahondagi eng so'ngi yangiliklar!\n")
    i = 1
    for x in uzb1 + jahon1 + iqtisod1 + jamiyat1 + fantex1 + sport1 + buscl1:
        title = x.text.strip()
        link = x.get('href')
        print("{}) <a href='https://kun.uz{}'>{}</a>".format(i, link, title))
        i += 1

kun('https://kun.uz/uz/news/category/uzbekiston', 'https://kun.uz/uz/news/category/jahon', 'https://kun.uz/uz/news/category/iktisodiet', 'https://kun.uz/uz/news/category/jamiyat', 'https://kun.uz/uz/news/category/tehnologia', 'https://kun.uz/uz/news/category/sport', 'https://kun.uz/uz/news/category/businessclass')  