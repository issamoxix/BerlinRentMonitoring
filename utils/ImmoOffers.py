from bs4 import BeautifulSoup
import requests
import json
from helpers.helper import *
import time
from datetime import datetime


headers = {
  'authority': 'www.immobilienscout24.de',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'referer': 'https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?numberofrooms=1.0-&price=-900.0&pricetype=calculatedtotalrent&sorting=2&enteredFrom=result_list',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
url = "https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?numberofrooms=1.0-&price=-900.0&pricetype=calculatedtotalrent&sorting=2&enteredFrom=result_list"


def ImmoCrawler():
    count = 0
    prev = [None for i in range(100)]
    while True:
        time.sleep(5)
        response = requests.get(url, timeout=15, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find("ul",{'id':'resultListItems'}).find_all('li',{'class':'result-list__listing'})

        for id,item in enumerate(items):
            title = item.find("h5").text
            if "NEU" in title:
                title = title.removeprefix("NEU")
            details_elem = item.find("div", {"class": "result-list-entry__criteria"}).find_all('dl')
            price = details_elem[0].find('dd').text
            size = details_elem[1].find('dd').text
            rooms = details_elem[2].find('dd').text
            offer = {
                "title":title,
                "price":price,
                "size":size,
                "rooms":rooms
            }
            # print(title,price,size,rooms)
            
            
            if offer != prev[id]:
                prev[id] = offer
                if count > 0:
                    alarm_soud()
        lastest = [prev[i] for i in range(5) if prev[i]]
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time, json.dumps(lastest[0], ensure_ascii=False))