import time
import urllib.parse
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib

# Shahre Ketab (book city) webpage.

webpage_url = "https://shahreketabonline.com"
products_url = '/all-products?field_filters=%7B%22item_group%22%3A%5B%22%DA%A9%D8%AA%D8%A7%D8%A8%22%5D%7D&price_range_filters=%7B%22price_range%22%3A%5B0%2C629000070%5D%7D&start=0'


# Title of webpage
def get_title_of_page():
    webpage_data = requests.get(webpage_url)
    soup = BeautifulSoup(webpage_data.content, "html.parser")

    title = soup.select_one("title")
    print(title.text)


# List of books
def get_books():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(webpage_url + products_url)

    print("Getting name of books...")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    products_title = soup.select('.product-title')

    for i in products_title:
        print(i.text.strip())


# Download Image of books
def get_image_of_books():
    driver = webdriver.Chrome()
    driver.maximize_window()

    print("Downloading Images, please wait...")

    driver.get(webpage_url + products_url)
    scroll_page(driver)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    image_tag = soup.findAll('img', 'card-img ls-is-cached lazyloaded')

    # get image urls
    img_urls = []
    for i in image_tag:
        url = urllib.parse.quote(i['src'])
        img_urls.append(webpage_url + url)

    # Save images on device
    counter = 1
    for i in img_urls:
        response = requests.get(i)
        content_type = response.headers.get("Content-type", "")
        ext = "bin"

        if content_type.startswith("image/"):
            ext = content_type.split("/")[-1]
        else:
            print(f"This link can't downloaded => {response.url}")

        filename = f"downloaded_image{counter}.{ext}"

        with open(filename, "wb") as f:
            f.write(response.content)
            print(f"Download file {counter} with url: {response.url} successfull")
            counter += 1

    driver.quit()


# scroll webpage for load images
def scroll_page(d):
    s = 10
    while True:
        d.execute_script(f"window.scrollTo(0, {s});")
        s += 10
        if s > 2500:
            time.sleep(5)
            break


get_title_of_page()
get_books()
get_image_of_books()
