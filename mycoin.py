import csv
import requests
from bs4 import BeautifulSoup
#ЗАПИСБ В ФАЙЛ ДАННЫХ
def data_csv(data):

    with open('coin.csv','a') as f:
        wiret = csv.writer(f)

        wiret.writerow([
            data['name'],
            data['url'],
            data['price']

        ])


#УБЕРАЕМ ДОЛЛАР
def red_price(pr):
    r = pr.replace('$','')
    return r 

 #ДЕЛАЕМ ВЫБОРКУ  ПО ТАБЛИЕЦЕ С КОИНТАМИ 
def data_html(data_text):
    soup = BeautifulSoup(data_text, 'lxml')
    tb = soup.find_all('table')[2].find('tbody').find_all('tr')

    for trs in tb:
        tds = trs.find_all('td')
        namecoint = tds[1].find('a', class_='cmc-link').text
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        price = tds[3].find('a').text
        price=red_price(price)
        
        data = {
            'name' : namecoint,
            'url' : url,
            'price' : price
        }
        data_csv(data)

        
# ПОЛУЧАЕМ ОТВЕТ ОТ САЙТА 
def html_resp(url):
    rec = requests.get(url)
    return rec.text
# ГЛАВНАЯ ФУНКЦИЯ
def main():
    print('GO PARSS!!!')
    url = 'https://coinmarketcap.com/'
    data_html(html_resp(url))
    print('THE END!!!')
 # ТАК НАДО :-)ДЫ
 
if __name__ == '__main__':
        main()
        