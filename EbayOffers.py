from bs4 import BeautifulSoup
import requests
import json
from helper import *
import time
from datetime import datetime


def main():
    url = "https://www.ebay-kleinanzeigen.de/s-wohnung-mieten/berlin/anzeige:angebote/c203l3331+wohnung_mieten.swap_s:nein"
    headers = {
        "authority": "www.ebay-kleinanzeigen.de",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "referer": "https://www.ebay-kleinanzeigen.de/s-wohnung-mieten/berlin/c203l3331+wohnung_mieten.swap_s:nein",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }

    count = 0
    prev = {}

    kill = True
    email_sent = []
    while kill:
        time.sleep(5)
        response = requests.get(url, timeout=15, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find("ul", {"id": "srchrslt-adtable"}).find_all(
            "li", {"class": ["lazyload-item", "ad-listitem"]}
        )
        item = [
            i
            for i in items
            if "is-topad" not in i.get("class") and "lazyload-item" in i.get("class")
        ][0]
        title = item.h2.text.strip()
        a_href = item.h2.a.get("href")
        price = item.find(
            "p", {"class": "aditem-main--middle--price-shipping--price"}
        ).text.strip()
        try:
            meta_data = [
                i.text
                for i in item.find("p", {"class": "text-module-end"}).find_all("span")
            ]
        except:
            meta_data = []
        offer = {
            "title": title,
            "price": price,
            "meta": meta_data,
            "href": f"https://www.ebay-kleinanzeigen.de{a_href}",
        }
        current_time = datetime.now().strftime("%H:%M:%S")
        if count > 0:
            if offer["href"] != prev["href"]:
                if offer['href'] in email_sent:
                    prev = offer
                    count += 1
                    print("[Ebay] ",current_time, json.dumps(offer, ensure_ascii=False))
                    continue
                print(
                    "[Ebay][NEW]",
                    current_time,
                    json.dumps(offer, ensure_ascii=False),
                )
                send_email(offer, f"[Ebay] {offer['title']}")
                email_sent.append(offer["href"])
        prev = offer
        count += 1
        print("[Ebay] ",current_time, json.dumps(offer, ensure_ascii=False))


if __name__ == "__main__":
    main()
