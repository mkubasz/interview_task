import re
from typing import Any, List
from urllib.request import urlopen
from bs4 import BeautifulSoup


def read_currency() -> List[str]:
    postfix_url: str = "https://www.ecb.europa.eu"
    web_content: str = urlopen("{}/home/html/rss.en.html".format(postfix_url))
    html_page: Any = BeautifulSoup(web_content, "html.parser")
    links_url: Any = html_page.select("a[href*=fxref-]")
    currencies: List[str] = []
    for link_url in links_url:
        web_content: str = urlopen("{}{}".format(postfix_url, link_url['href']))
        html_page = BeautifulSoup(web_content, "html.parser")
        currencies.append(re.search(r"(\d+\.\d+) ([A-Z]{3})", html_page.text).group())  # Parse currency N.NNN USD
    return currencies

def save_to_db(currencies: List[str]):
    return True


if __name__ == "__main__":
    save_to_db(read_currency())
