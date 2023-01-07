from enum import Enum
from stock_indicators import indicators
from stock_indicators import CandlePart

indicatorList = []

class listOfIndicators(Enum):
    SMA = "SMA"


indicatorList.append(listOfIndicators.SMA)

def getIndicator(indicatorNum, stock):
    returnVal = None

    if (indicatorNum==0): returnVal = getSMA(stock)

    return returnVal

def getSMA(stock):
    lookBackPeriod = input("Please enter the look back period.")
    results =  indicators.get_sma(stock, lookBackPeriod, CandlePart.CLOSE)
    return results
