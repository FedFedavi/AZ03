
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv


driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get('https://www.divan.ru/izhevsk/category/divany-i-kresla')

    # Даем странице загрузиться
    time.sleep(5)

    # Парсим цены
    prices = driver.find_elements("css selector", ".q5Uds.T7z9Z.fxA6s span")

    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок

        # Записываем каждую цену в файл
        for price in prices:
            writer.writerow([price.text])


finally:
    # Закрываем драйвер
    driver.quit()
