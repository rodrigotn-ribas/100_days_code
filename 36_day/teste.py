from newsapi import NewsApiClient
from requests import Response
import requests
import requests_cache

# # Init
# newsapi = NewsApiClient(api_key='8732cf1fcf3d4675a3ff3f6c8a06fd7d')
#
# # # /v2/top-headlines
# # top_headlines = newsapi.get_top_headlines(q="Tesla",
# #                                           sources='bbc-news,the-verge',
# #                                           language='en')
#
# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()
# print(sources)

API_KEY = "8732cf1fcf3d4675a3ff3f6c8a06fd7d"

URL = "https://newsapi.org/v2/everything"

parameters = {
    "q" : "tesla",
    "apikey" : API_KEY
}

requests_cache.install_cache('Tesla_News', expire_after=3000)

response: Response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
is_from_cache = getattr(response, 'from_cache', False)
source: str = 'CACHE' if is_from_cache else 'API'

print(f"{source}\n{data}")
