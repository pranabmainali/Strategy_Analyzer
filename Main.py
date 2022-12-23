import YFinance

api_key = "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a"

def getHistoricalData(ticker, interval):
    link = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/hi/history/"+ticker+"/"+interval
    print(YFinance.getRequests(link, api_key).text)

getHistoricalData("MSFT", "1d")

#def setStock(ticker, interval):
