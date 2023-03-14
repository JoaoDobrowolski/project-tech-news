from tech_news.database import db
from datetime import datetime


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
    # https://stackoverflow.com/questions/48750212/how-can-i-check-if-a-date-field-is-in-iso-format
    try:
        date_correct_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": date_correct_format}
        search = [(index['title'], index['url'])
                  for index in db.news.find(query)]
        # print(">>>>>>>>", search)
        return search
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    query = {
        "category": {
            "$regex": category,
            "$options": 'i'}}
    search = [(index['title'], index['url']) for index in db.news.find(query)]
    # print(">>>>>>", search)
    return search
