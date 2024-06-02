# import requests
#
# r = requests.get("https://ru.wordpress.org/")
# print(r.content)
import csv

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text.encode("utf-8")
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == "__main__":
#     main()


# import re
# import requests
# from bs4 import BeautifulSoup
# import csv


# def get_html(url):
#     r = requests.get(url)
#     return r.text.encode("utf-8")
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator='\n', delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[-1]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name,
#                 'url': url,
#                 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     (get_data(get_html(url)))


# if __name__ == "__main__":
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text.encode("utf-8")
#
#
# def refine_cy(s):
#     return s.split()
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except AttributeError:
#             name = ""
#             print("Error")
#
#         try:
#             url = el.find("h3").find("a")['href']
#         except AttributeError:
#             url = ""
#             print("Error")
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except AttributeError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#
#         write_csv(data)
#
#
# def write_csv(data):
#     with open("plugins block.csv", 'a', encoding='windows-1251') as file:
#         writer = csv.writer(file, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def main():
#     for i in range(24, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}"
#         get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()


from parsers import Parser


def main():
    pars = Parser("https://www.ixbt.com/live/index/news/", 'news.txt')
    pars.run()


if __name__ == "__main__":
    main()
