from helpers.helper import send_email
from utils import EbayCrawler, WgCrawler
import threading
from datetime import datetime


def start_crawling():
    current_time = datetime.now().strftime("%H:%M")
    start_text = f"Crawling Started at {current_time}"
    send_email(start_text, f"[{current_time}] Sniffig Rents")

    t1 = threading.Thread(target=EbayCrawler)
    t2 = threading.Thread(target=WgCrawler)

    # start the threads
    t1.start()
    t2.start()

    # wait for the threads to finish
    t1.join()
    t2.join()


if __name__ == "__main__":
    start_crawling()
