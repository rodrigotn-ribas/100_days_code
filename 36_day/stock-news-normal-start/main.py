from requests import Response
import requests
import requests_cache


# ====== Constants ======= #
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_API_KEY = "XZORCMOGIKBCVDCX"
NEWS_API_KEY = "8732cf1fcf3d4675a3ff3f6c8a06fd7d"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

stock_market_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : ALPHAVANTAGE_API_KEY
}

requests_cache.install_cache('Tesla_stock_market', expire_after=3000)

response: Response = requests.get(STOCK_ENDPOINT, params=stock_market_parameters)
response.raise_for_status()
data = response.json()
is_from_cache = getattr(response, 'from_cache', False)
source: str = 'CACHE' if is_from_cache else 'API'

print(f"\n{source}\n{data}")

daily_stock_prices = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday = daily_stock_prices[0]['4. close']

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday = daily_stock_prices[1]['4. close']


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday)-float(day_before_yesterday))
# print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

print(f"yesterday: {yesterday}, day before yesterday {day_before_yesterday}, difference: {difference:.4f}")

# 10% de 1000 = 1000 * 0.1 or 100 / 0.1; 1000 / 100
percent = difference / float(yesterday) * 100

print(f"{percent:.2f}%")

#TODO 5. - TODO4 If percentage is greater than 5 then print("Get News").

if percent > 5:
    print("Get News")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


news_parameters = {
    "q" : COMPANY_NAME,
    "apikey" : NEWS_API_KEY
}

requests_cache.install_cache('Tesla_News', expire_after=3000)

response: Response = requests.get(NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
data = response.json()
is_from_cache = getattr(response, 'from_cache', False)
source: str = 'CACHE' if is_from_cache else 'API'


print(f"\n{source}\n{data}")


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

articles = [value for (key, value) in data["articles"][0].items()]
print(articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

