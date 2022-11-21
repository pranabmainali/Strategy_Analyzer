import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL,MSFT"

headers = {
	"X-RapidAPI-Key": "e12d9d9af3mshcb72c7f3893119bp129decjsn38df9d01169a",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

