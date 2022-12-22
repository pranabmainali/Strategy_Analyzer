import requests 

api_key = "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a"

def getRequests(url, api_key):
    querystring = {"diffandsplits":"false"}

    headers = {
    	"X-RapidAPI-Key": "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a",
    	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

