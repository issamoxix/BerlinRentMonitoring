# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.firefox.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?numberofrooms=1.0-&price=-900.0&pricetype=calculatedtotalrent&sorting=2&enteredFrom=result_list")
#     print(page.title())
#     browser.close()

import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as gui 
import random

driver = uc.Chrome()
url = "https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?numberofrooms=1.0-&price=-900.0&pricetype=calculatedtotalrent&sorting=2&enteredFrom=result_list"
driver.get(url)
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "geetest_btn"))
    )
time.sleep(3)
count = 0

while True:
    if count == 10:
        break
    gui.moveTo(random.randint(100, 700),random.randint(200, 700))
    gui.moveTo(200,random.randint(200, 700))
    x,y = gui.position()
    if x != 200:
        break
    count += 1



driver.execute_script("""const target = document.getElementsByClassName('geetest_btn')[0];
const mouseEvent = new MouseEvent('mousemove', {
  clientX: 100, // x-coordinate of the mouse pointer
  clientY: 200 // y-coordinate of the mouse pointer
});
target.dispatchEvent(mouseEvent);
console.log(mouseEvent)""")
driver.find_element_by_css_selector('div.geetest_btn').click()
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul#resultListItems"))
    )
print('Done !')
# // get the element on which the mouse movement will be simulated
# const target = document.getElementById('my-element');

# // create a new mouse event
# const mouseEvent = new MouseEvent('mousemove', {
#   clientX: 100, // x-coordinate of the mouse pointer
#   clientY: 200 // y-coordinate of the mouse pointer
# });

# // dispatch the mouse event on the target element
# target.dispatchEvent(mouseEvent);
