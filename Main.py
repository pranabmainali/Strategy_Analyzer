import YFinance
from stock_indicators.indicators.common.quote import Quote
import json

api_key = "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a"

def getHistoricalData(ticker, interval):
    link = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/hi/history/"+ticker+"/"+interval
    return YFinance.getRequests(link, api_key).text

#getHistoricalData("MSFT", "1d")

def get_historical_quotes(ticker, interval):
    quotes = None

    print(getHistoricalData(ticker, interval))

    #returnData = json.loads(getHistoricalData(ticker, interval))
    #print(returnData)
    #for item in returnData['items']:
    #    print(item)

get_historical_quotes("MSFT", "1d")
    

