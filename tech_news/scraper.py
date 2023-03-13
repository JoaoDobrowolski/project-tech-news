import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
