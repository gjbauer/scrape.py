#!/usr/bin/python3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://archive.org/")

'''
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "#product-grid .product-item")
    )
)
'''

html = driver.page_source

print(html)

driver.quit()

soup = BeautifulSoup(html, 'html.parser')

item = soup.find_all("title", {})

print(item)

for x in item:
    print(x.text)
