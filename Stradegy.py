import YFinance


name = None
stock = None
buyCondition = []
sellCondition = []
maximumDataConverageDate = None

def __init(self, name):
    self.name = name

def addStock(self, ticker, interval):
    self.stock = YFinance.get_historical_quotes(ticker, interval)
    self.maximumDataCoverageDate = self.stock[0].date
    return self.maximumDataConverageDate


    