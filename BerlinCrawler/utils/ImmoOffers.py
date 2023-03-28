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
  'cookie': 'seastate="TGFzdFNlYXJjaA==:ZmFsc2UsMTY3OTc4MTkzNTk4NiwvZGUvYmVybGluL2Jlcmxpbi93b2hudW5nLW1pZXRlbj9udW1iZXJvZnJvb21zPTEuMC0mcHJpY2U9LTkwMC4wJnByaWNldHlwZT1jYWxjdWxhdGVkdG90YWxyZW50"; feature_ab_tests="DiscoveryTests@15=Default"; ABNTEST=1677189776; is24_experiment_visitor_id=9050cb5c-3060-4be0-a5e3-8bfb0f680228; is24_search_experiment_visitor_id=0be09303-bf02-45b2-826b-b32854cc5e52; optimizelyUniqueVisitorId=66af20d3-135c-4a42-80b6-d2734b817593; _gcl_au=1.1.426371099.1677189781; ssoOptimizelyUniqueVisitorId=bc64049a-c48c-4980-be0c-31793d451413; IS24VisitId=viddc209189-0e61-4db8-90f7-af1d3b0ca2ed; optimizelyEndUserId=oeu1677878349831r0.5026138274594101; _gid=GA1.2.1483439850.1679597496; consent_status=true; _clck=1futv29|1|fa7|0; ln_or=eyI2NTc4OTciOiJkIiwiMTI4OTU5MyI6ImQifQ%3D%3D; AWSALB=xe56yipC8MRhoNCDyfYTNnWdxlmIbBvadFDkE9ri+lxgzCMpJoPoluBjnKoRMP8bjNqm16Gx9M8F0g4iM81s9ZLnKLtAY79NNLhtM6uO7F3xr+ggi9UaSiT0/HAX; AWSALBCORS=xe56yipC8MRhoNCDyfYTNnWdxlmIbBvadFDkE9ri+lxgzCMpJoPoluBjnKoRMP8bjNqm16Gx9M8F0g4iM81s9ZLnKLtAY79NNLhtM6uO7F3xr+ggi9UaSiT0/HAX; user-info=eyJzc29JZCI6MTI0MDY4OTIzLCJlbWFpbCI6Imlzc2FtaGFpZGFvdWlAZ21haWwuY29tIiwiY2FuSGlkZURwYUNoZWNrYm94Ijp0cnVlfQ==; reese84=3:tO0esLqU2UAiRt8XPijG7w==:YGDaQ0mwkSVeEkpvxj4Nv7vBERkeWBoUAPvI+xFY/iQa3n5z+Wz6macpBV+Q1FCMWABaRo9OJ4sJvb9aJuND2mUuIMonoH55zxLbbW5t9HPCINbbmHGWcmBvQXR4uMWSxdRLvSN/F3mr6auMpiVk9PvIfhq7UbELoorybPstgCiC4usdB0Ba+JG32mTDG/7ECIZqOHMNG1eX9hRrfkuWOVG31Io5jmPBijQCSzHNMIpN9nXEKj6WECz2l6YbGSM8VzicnSQMcUYnpc5jawBQ7pjwFjFGsopEuJYx00HTlGLIcoeXcQicu5x5QL28Gtmem5HBcUELtulK9BqNPVJSVjH1CBNf1uExJsZdbyCIs5TjKBGtC7qWMZKBacKzbePotZhoYx8qfygeAN0awPw2SHqSKyezrX5MZEg9RESDgsFrhjhW3kTSZZG9rD5tEn4HSo9j8MksfGA1jN0kyPpp1D3kDtodKJoAINivIPttdoupGvrpMifjfNiwRJQedZB4vAkXMJaYpAWOGNEzi3RY7g==:Nxvd+NVydeRRL1Xs+MEf6kDO++vGS0oex13t5C1i4EU=; longUnreliableState="dWlkcg==:MTI0MDY4OTIz"; _tq_id.TV-27098109-1.3d49=f00d2e37b605c248.1677189781.0.1679781938..; _uetsid=bcc18420c9ab11edb804e14b0d8f8893; _uetvid=8844890011df11ed8c2eb1be92b6747a; _ga_BFT95EK8KY=GS1.1.1679767451.83.1.1679781938.0.0.0; _ga=GA1.2.1512275532.1677189781; utag_main=v_id:0186804d0dbe0017dc101041ba600506f002106700fb8$_sn:84$_se:113$_ss:0$_st:1679783738828$psn_usr_login_cookie:true%3Bexp-1711280698325$cdp_ab_splittest:GroupB$dc_visit:83$utm_source_30d:system%3Bexp-1681681237092$ses_id:1679767447535%3Bexp-session$_pn:29%3Bexp-session$referrer_to_lp:%3Bexp-session$ga_cd_cxp_referrer:RESULT_LIST%3Bexp-session$dc_event:46%3Bexp-session$dc_region:eu-central-1%3Bexp-session$geo_bln_session:berlin%3Bexp-session$geo_krs_session:berlin%3Bexp-session$ga_cd_application_requirements:profile0%3Bexp-session$ga_cd_test_cxp_expose:R8N_582_PLZBOX_V2%3Bexp-session$obj_listFirstStatus:false%3Bexp-session$obj_privateOffer:true%3Bexp-session$survey_overlay:b%3Bexp-session; _clsk=19wmyvn|1679781938930|34|0|p.clarity.ms/collect; seastate="TGFzdFNlYXJjaA==:ZmFsc2UsMTY3OTc4MjU1ODY4NywvZGUvYmVybGluL2Jlcmxpbi93b2hudW5nLW1pZXRlbj9udW1iZXJvZnJvb21zPTEuMC0mcHJpY2U9LTkwMC4wJnByaWNldHlwZT1jYWxjdWxhdGVkdG90YWxyZW50"',
  'referer': 'https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?numberofrooms=1.0-&price=-900.0&pricetype=calculatedtotalrent&sorting=2&enteredFrom=result_list',
  'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
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