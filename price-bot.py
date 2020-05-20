import requests
from bs4 import BeautifulSoup
from datetime import date


def amazon_parser(soup):
    title = soup.find(id="productTitle").get_text().strip()
    rawPrice = soup.find(id="priceblock_ourprice").get_text().strip()
    price = float(rawPrice[:-2].replace(",", "."))
    return (date.today(), title, price)


def load_product_info(url, parser):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup = BeautifulSoup(soup1.prettify(), "html.parser")
    return parser(soup)


def format_csv(data):
    return "{0}, \"{1}\", {2}".format(*data)


print(format_csv(load_product_info(
    "https://www.amazon.de/dp/B075D98BF8/?coliid=I11E7D5EZH93MT&colid=166XE3PZ8N0B7&psc=1&ref_=lv_ov_lig_dp_it", amazon_parser)))
print(format_csv(load_product_info(
    "https://www.amazon.de/MSI-5700-GAMING-Grafikkarte-DisplayPort/dp/B07XSJ2F8S/ref=sr_1_13", amazon_parser)))
