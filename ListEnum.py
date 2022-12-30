from enum import Enum

class conditionEnum(Enum):
    conditionEnumList = []

    LESSTHAN = "<"
    LESSTHANEQUAL = "<="
    EQUAL = "=="
    MORETHANEQUAL = ">="
    MORETHAN = ">"

    conditionEnumList.append(LESSTHAN)
    conditionEnumList.append(LESSTHANEQUAL)
    conditionEnumList.append(EQUAL)
    conditionEnumList.append(MORETHANEQUAL )
    conditionEnumList.append(MORETHAN)

class IntervalEnum(Enum):
    FIVEMINUTE = '5m'
    FIFTEENMINUTE = '15m'
    THIRTYMINUTE = '30m'
    ONEHOUR = '1h'
    ONEDAY = '1d'
    ONEWEEK = '1wk'