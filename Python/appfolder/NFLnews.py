import requests
from newsapi import NewsApiClient
import json



url = "https://newsapi.org/v2/everything?sources=nfl-news&sortBy=publishedAt&apiKey=19bd266db0094bc9b20fffac8d5352a7"

r = requests.get(url)
response = json.loads(r.text)
news = response['articles']

for i in range(len(news)):
    val = [
    str(news[i]['author']),
    str(news[i]['title']),
    str(news[i]['content']),
    str(news[i]['publishedAt'])
    ]
    print("Author: ", val[0], "\nTitle: ", val[1], "\nContent: ", val[2], "\nPublished at: ", val[3])
    

