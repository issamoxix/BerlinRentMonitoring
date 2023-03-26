from bs4 import BeautifulSoup
import requests
import json
from helper import *
from datetime import datetime
import re


def main():
    headers = {}
    url = "https://www.wg-gesucht.de/1-zimmer-wohnungen-in-Berlin.8.1.1.0.html?csrf_token=095e31362ff134f5e3e5a8b3c8971281caf48fbd&offer_filter=1&city_id=8&sort_order=0&noDeact=1&categories%5B%5D=1&rent_types%5B%5D=2&rent_types%5B%5D=2&exc=2"

    count = 0
    prev = {}

    kill = True
    while kill:
        response = requests.get(url, timeout=15, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        soup.select("div#liste-details-ad-9974091 h3.truncate_title > a")[0].text
        item = soup.find("div", {"id": re.compile("liste-details-ad-\d")})
        title = item.find("h3").text
        title = title.strip()
        a_href = item.find("h3").a.get('href')
        details = item.find("div", {"class": "row noprint middle"}).find_all("b")
        price = details[0].text
        size = details[1].text
        offer = {
            "title": title,
            "price": price,
            "size": size,
            "href":f"https://www.wg-gesucht.de{a_href}"
        }
        current_time = datetime.now().strftime("%H:%M:%S")
        if count > 0:
            if offer["href"] != prev["href"]:
                print(
                    "[NEW]",
                    current_time,
                    json.dumps(offer, ensure_ascii=False),
                )
                send_email(offer, f"[WGG] {offer['title']}")
        prev = offer
        count += 1
        print(current_time, json.dumps(offer, ensure_ascii=False))



        

if __name__ == "__main__":
    main()
