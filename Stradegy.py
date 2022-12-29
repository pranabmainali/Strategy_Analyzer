import YFinance
from stock_indicators.indicators.common.quote import Quote

class Stradegy:
    name = None
    stock = None
    buyCondition = []
    sellCondition = []
    maximumDataConverageDate = None

    def __init__(self, name):
        self.name = name

    def addStock(self, ticker, interval):
        self.stock = YFinance.get_historical_quotes(ticker, interval)
        print(self.stock[0].use())
        self.maximumDataCoverageDate = self.stock[0].da
        return self.maximumDataConverageDate


    