import requests 
import json
from stock_indicators.indicators.common.quote import Quote

api_key = "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a"

def getRequests(url, api_key):
    querystring = {"diffandsplits":"false"}

    headers = {
    	"X-RapidAPI-Key": "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a",
    	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def getHistoricalData(ticker, interval):
    link = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/hi/history/"+ticker+"/"+interval
    return getRequests(link, api_key).text

#getHistoricalData("MSFT", "1d")

def get_historical_quotes(ticker, interval):

    returnData = json.loads(getHistoricalData(ticker, interval))
    for item in returnData['items']:
        date = returnData['items'][item]['date']
        open = returnData['items'][item]['open']
        high = returnData['items'][item]['high']
        low = returnData['items'][item]['low']
        close = returnData['items'][item]['close']
        volume = returnData['items'][item]['volume']
        quote = Quote(date, open, high, low, close, volume)
        return quote

get_historical_quotes("MSFT", "1d")

