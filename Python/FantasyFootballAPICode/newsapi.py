from newsapi import NewsApiClient



newsapi = NewsApiClient(api_key = "19bd266db0094bc9b20fffac8d5352a7")

top_headlines = newsapi.get_top_headlines(
q='NFL', 
sources='espn', 
category='sports', 
language='en', 
country= 'us')


print(top_headlines)