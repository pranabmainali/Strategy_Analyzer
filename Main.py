import YFinance

self 

def getHistoricalData(ticker, interval):
    link = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/hi/history/"+ticker+"/"+interval
    print(YFinance.getRequests(link, api_key).text)

getHistoricalData("MSFT", "1d")