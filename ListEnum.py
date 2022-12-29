from enum import Enum

class conditionEnum(Enum):
    LESSTHAN = "<"
    LESSTHANEQUAL = "<="
    EQUAL = "=="
    MORETHANEQUAL = ">="
    MORETHAN = ">"

class IntervalEnum(Enum):
    FIVEMINUTE = '5m'
    FIFTEENMINUTE = '15m'
    THIRTYMINUTE = '30m'
    ONEHOUR = '1h'
    ONEDAY = '1d'
    ONEWEEK = '1wk'