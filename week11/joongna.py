from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://web.joongna.com/search?keyword=%EC%95%84%EC%9D%B4%ED%8F%B013&page=1")

time.sleep(1)
textbox = browser.find_elements(By.CLASS_NAME, "ant-col.col.css-t7ixlq.e312bqk0")

for e in textbox:
    price_element = e.find_element(By.CLASS_NAME, "priceTxt")
    print(price_element.text)
