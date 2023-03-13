import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    HEADERS = {"user-agent": "Fake user-agent"}
    time.sleep(1)

    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".archive-main h2 a::attr(href)").getall()
    # print(">>>>>>>>>>>>", urls)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".next::attr(href)").get()
    # print(">>>>>>>>>>>>", (next_page_url))
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    # ou poderia pegar o link pelo botão share da página ao fazer um split
    title = (selector.css(".entry-title::text").get()).strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = selector.css(".meta-reading-time::text").get()
    reading_time = int(re.sub('[^0-9]', '', reading_time))
    # https://pt.stackoverflow.com/questions/254748/remover-caracteres-n%C3%A3o-num%C3%A9ricos-de-uma-string-em-python
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    summary = (''.join(summary)).strip()
    category = selector.css(".category-style .label::text").get()

    news = {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': reading_time,
        'summary': summary,
        'category': category,
    }

    # print(">>>>>>>>>>>>", (news))
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
