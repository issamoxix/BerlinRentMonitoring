from bs4 import BeautifulSoup
import requests
import json
from helpers.helper import *
from datetime import datetime
import re


def WgCrawler():
    headers = {}
    url = "https://www.wg-gesucht.de/1-zimmer-wohnungen-in-Berlin.8.1.1.0.html?csrf_token=095e31362ff134f5e3e5a8b3c8971281caf48fbd&offer_filter=1&city_id=8&sort_order=0&noDeact=1&categories%5B%5D=1&rent_types%5B%5D=2&rent_types%5B%5D=2&exc=2"

    count = 0
    prev = {}

    kill = True
    email_sent = []
    while kill:
        try:
            response = requests.get(url, timeout=15, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            item = soup.find("div", {"id": re.compile("liste-details-ad-\d")})
            title = item.find("h3").text
            title = title.strip()
            a_href = item.find("h3").a.get('href')
            details = item.find("div", {"class": "row noprint middle"}).find_all("b")
            price = details[0].text
            try:
                size = details[1].text
            except:
                size = None
            offer = {
                "title": title,
                "price": price,
                "size": size,
                "href":f"https://www.wg-gesucht.de{a_href}"
            }
            current_time = datetime.now().strftime("%H:%M:%S")
            if count > 0:
                if offer["href"] != prev["href"]:
                    if offer['href'] in email_sent:
                        prev = offer
                        count += 1
                        print("[WGG] ",current_time, json.dumps(offer, ensure_ascii=False))
                        continue
                    print(
                        "[WGG][NEW]",
                        current_time,
                        json.dumps(offer, ensure_ascii=False),
                    )
                    send_email(offer, f"[WGG] {offer['title']}")
                    email_sent.append(offer["href"])
            prev = offer
            count += 1
            print("[WGG] ",current_time, json.dumps(offer, ensure_ascii=False))
        except Exception as e:
            print(f'[ERROR] something went wrong {e}')

