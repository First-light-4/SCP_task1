import shutil
import os
from selenium import webdriver
from datetime import datetime
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup


def get_products(url, name):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    with open(f"{name}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open(f"{name}.html", "r", encoding="utf-8") as file:
        src = file.read()

    return src

def get_data_with_selenium(url):

    options = webdriver.ChromeOptions()

    options.add_argument(f"user-agent={UserAgent().ie}")
    # options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    # without window
    # options.headless = True

    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(executable_path=r"chromedriver.exe",
                              options=options)
    driver.get(url=url)
    time.sleep(15)
    return driver

def main():
    url = 'https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204?webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts'
    try:
        # обьявление всех списков и создание всех папок
        os.mkdir('people')
        os.mkdir('cloths')
        all_hrefs = []
        driver = get_data_with_selenium(url)


        # only Polo Ralph Lauren
        url_polo = driver.find_element(By.ID, 'brandpolo_ralph_lauren').get_attribute('href')
        driver.quit()
        driver = get_data_with_selenium(url_polo)
        src = driver.page_source
        driver.quit()

        soup = BeautifulSoup(src, "lxml")
        all = soup.find_all(class_='name-link')
        for i in all:
            href = f'https://www.ralphlauren.nl/{i["href"]}'
            all_hrefs.append(href)
            print(href)
        url_polo = soup.find(class_="more-button button inverse")['href']

        # цикл для получения ссылок на все товары со всех страниц
        while True:
            driver = get_data_with_selenium(url_polo)
            src = driver.page_source
            driver.quit()

            soup = BeautifulSoup(src, "lxml")
            all = soup.find_all(class_='name-link')
            for i in all:
                href = f'https://www.ralphlauren.nl/{i["href"]}'
                all_hrefs.append(href)
                print(href)

            try:
                url_polo = soup.find(class_="more-button button inverse")['href']
            except Exception as ex:
                print(ex)
                break
            finally:
                driver.quit()
        print(all_hrefs)
        print(len(all_hrefs))

        #получение фотографий с сайта
        for i in range(len(all_hrefs)):
            while True:
                try:
                    driver = get_data_with_selenium(all_hrefs[i])
                    src = driver.page_source
                    driver.quit()

                    soup = BeautifulSoup(src, "lxml")
                    img1 = soup.find_all(class_='swiper-zoomable')[0]['data-highres-images']
                    response = requests.get(img1, stream=True)
                    with open(f'people\img{i}.png', 'wb') as file:
                            shutil.copyfileobj(response.raw, file)
                    del response

                    img2 = soup.find_all(class_='swiper-zoomable')[1]['data-highres-images']
                    response = requests.get(img2, stream=True)
                    with open(f'cloths\img{i}.png', 'wb') as file:
                        shutil.copyfileobj(response.raw, file)
                    del response
                except Exception as ex:
                    print(ex)
                else:
                    break

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
