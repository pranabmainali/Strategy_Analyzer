import YFinance
from stock_indicators.indicators.common.quote import Quote

class Stradegy:
    name = None
    stock = None
    candles = None
    buyCondition = []
    sellCondition = []
    maximumDataConverageDate = None

    def __init__(self, name):
        self.name = name

    def addStock(self, ticker, interval):
        self.stock, self.candles = YFinance.get_historical_quotes(ticker, interval)
        self.maximumDataConverageDate = self.candles[0].date
        return self.maximumDataConverageDate

    def addBuyCondition(self, condition):
        self.buyCondition.append(condition)

    def addSellCondition(self, condition):
        self.sellCondition.append(condition)

    def runStradegy():
        return 0

mainStradegy = Stradegy("firstStradegy")
mainStradegy.addStock("MSFT", "5m")
    