from urllib.request import urlopen
from bs4 import BeautifulSoup

web_content: str = urlopen("https://www.ecb.europa.eu/home/html/rss.en.html")
html_page = BeautifulSoup(web_content)
print(html_page)