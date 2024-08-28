
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv


driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get('https://izhevsk.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/')

    # Даем странице загрузиться
    time.sleep(5)

    # Парсим цены
    prices = driver.find_elements(By.CSS_SELECTOR, "div[data-name='CardPriceBlock'] span.aee5b7c44e--color_black_100--Ephi7")

    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок

        # Записываем каждую цену в файл
        for price in prices:
            writer.writerow([price.text])


finally:
    # Закрываем драйвер
    driver.quit()
