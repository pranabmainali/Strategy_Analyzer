import ListEnum

class Condition:
    firstValue = None
    secondValue = None
    condition = None

    def __init__(self, firstValue, condition, secondValue):
        self.firstValue = firstValue
        self.secondValue = secondValue
        self.condition = condition

