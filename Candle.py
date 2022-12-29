
class Candle():
    date = None
    open = None
    high = None
    low = None
    close = None
    volume = None

    def __init__(self, date, open, high, low, close, volume):
        self.date = date
        self.open = open
        self.high = high
        self.low = low 
        self.close = close 
        self.volume = volume
        