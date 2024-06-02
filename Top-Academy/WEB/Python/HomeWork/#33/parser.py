from bs4 import BeautifulSoup
import requests as rs


def get_html(url):
    r = rs.get(url)
    return r.text.encode("utf-8")


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    price = soup.find("span", class_="jxpCgO").text
    return price


s = "https://coinmarketcap.com/currencies/toncoin/"
print(get_data(get_html(s)))
