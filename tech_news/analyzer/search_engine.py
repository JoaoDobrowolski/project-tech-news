from tech_news.database import db


# Requisito 7
def search_by_title(title):
    # https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
    query = {
        "title": {
            "$regex": title,
            "$options": 'i'}}
    search = [(index['title'], index['url']) for index in db.news.find(query)]
    # print(">>>>>>", search)
    return search


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
