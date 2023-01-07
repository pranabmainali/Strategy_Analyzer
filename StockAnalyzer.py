from Stradegy import Stradegy
import Indicator
from Indicator import listOfIndicators
from ListEnum import conditionEnum
from Condition import Condition

stradegyList = []
game = True

print("Welcome to the Stock Analyzer program!")
print(" ")

def addCondition(stradegyNum):
    print("Please choose the number for which the indicator you want to set as condition")
    for i in range(len(Indicator.indicatorList)):
        print(i,". ",Indicator.indicatorList[i].value)
    indicatorNum = input()
    firstIndicator = Indicator.getIndicator(indicatorNum)


    print("Please choose the number for the following")
    for i in range(len(conditionEnum.conditionEnumList)):
        print(i,". ",conditionEnum.conditionEnumList[i])
    conditionNum = input()
    conditionVal = conditionEnum.conditionEnumList[i]


    print("Please choose the number for which condition you want to use")
    for i in range(len(Indicator.indicatorList)):
        print(i,". ",Indicator.indicatorList[i].value)
    indicatorNum = input()
    secondIndicator = Indicator.getIndicator(indicatorNum)

    currentCondition = Condition(firstIndicator, conditionVal, secondIndicator)

    return currentCondition

def changeBuyCondition(conditions, stradegyNum):
    buyConditions = conditions
    userInput = None
    if (len(buyConditions)==0):
        userInput = input("You currently dont have any conditions, Press A to add, or X to go back")
    else:
        print("Here are your current buy conditions : ")
        for condition in buyConditions:
            print(condition.stringVersion)
        userInput = input("Enter the condition number to make changes to it. Or press a to add condition, or press x to exit")
    userInput = userInput.capitalize()

    if userInput=="A":
        buyConditions.append(addCondition(stradegyNum))

    return buyConditions
    

def changeSellCondition(conditions, stradegyNum):
    sellConditions = conditions
    userInput = None
    if (len(sellConditions)==0):
        userInput = input("You currently dont have any conditions, Press A to add, or X to go back")
    else:
        print("Here are your current sell conditions : ")
        for condition in sellConditions:
            print(condition.stringVersion)
        userInput = input("Enter the condition number to make changes to it. Or press a to add condition, or press x to exit")
    userInput = userInput.capitalize()

    if userInput=="A":
        sellConditions.append(addCondition(stradegyNum))

    return sellConditions


def createStradegy():
    stradegyName = input("What is this stradegy going to be called?")
    currentStradegy = Stradegy(stradegyName)
    currentStradegyNum = len(stradegyList) 
    stock = input("Please enter your stock's ticker symbol . Example (MSFT)")
    stock = stock.capitalize()
    interval = input("Please input the interval in which you want your data. One of (5m, 15m, 30m, 1h, 1d, 1wk, 1mo, 3mo)")
    maiximumCoverageDate = currentStradegy.addStock(stock, interval)
    print("Please note that only data as far back as "+maiximumCoverageDate.strftime("%B %d, %Y")+" can be tested on!")
    userInput = None
    if (len(currentStradegy.buyCondition)==0 or len(currentStradegy.sellCondition)==0):
        userInput = input("Please add at least one buy condition and one sell condition. Press (s for sell condition, b for buy condition, x to stop creating this stradegy")
    else:
        userInput = input("Press (s to change sell condition, b to change buy condition, and x to run stradegy")

    userInput = userInput.lower()
    if (userInput == "s"):
        currentStradegy.sellCondition = changeSellCondition(currentStradegy.sellCondition, currentStradegyNum)
    elif (userInput == "b"):
        currentStradegy.buyCondition = changeBuyCondition(currentStradegy.buyCondition, currentStradegyNum)
    elif (userInput == "x"):
        if (len(currentStradegy.buyCondition)>0 and len(currentStradegy.sellCondition)>0):
            stradegyReport = currentStradegy.run()

def endProgram():
    print("Bye Bye!")

while game==True:
    if len(stradegyList) == 0:
        createNewStradegyPrompt = True
        while createNewStradegyPrompt==True:
            createNewStradegy = input("It seems you do not have any stradegies right now, would you like to create a new stradegy? Press (Y for yes / N for no)")
            createNewStradegy = createNewStradegy.lower()
            if createNewStradegy=="y":
                createStradegy()
                createNewStradegyPrompt = False
            elif createNewStradegy =="n":
                endProgram()
                game=False
                createNewStradegyPrompt = False
            else:
                print("Please enter a valid input value.")

