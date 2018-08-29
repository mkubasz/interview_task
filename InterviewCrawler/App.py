import re
import time
import os
from typing import Any, List
from urllib.request import urlopen
from bs4 import BeautifulSoup
import schedule
import sqlite3


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
    pwd = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../InterviewApi/db.sqlite3'))
    conn = sqlite3.connect(pwd)
    c = conn.cursor()
    c.execute('DELETE FROM api_currency')
    conn.commit()
    sql = ''' INSERT INTO api_currency(name,value)
                  VALUES(?,?) '''
    for currency in currencies:
        c.execute(sql, (currency.split(" ")[1], currency.split(" ")[0]))
    conn.commit()
    conn.close()
    return True


def job():
    save_to_db(read_currency())


if __name__ == "__main__":
    save_to_db(read_currency())
    # schedule.every().day.at("15:16").do(job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)  # wait one minute
