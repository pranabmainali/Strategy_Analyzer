from Stradegy import Stradegy
import Indicator
from Indicator import listOfIndicators
from ListEnum import conditionEnum

stradegyList = []
game = True

print("Welcome to the Stock Analyzer program!")
print(" ")

def addCondition():
    print("Please choose the number for which the indicator you want to set as condition")
    for i in range(len(Indicator.listOfIndicators)):
        print(i+". "+Indicator.listOfIndicators[i].value)
    indicatorNum = input()

    #This is where the methods will be called to add indicators

    #between
    print("Please choose the number for which condition you want to use")
    for i in range(len(Indicator.listOfIndicators)):
        print(i+". "+Indicator.listOfIndicators[i].value)
    indicatorNum = input()



def changeBuyCondition(currentStradegy):
    userInput = None
    if (len(currentStradegy.buyConditions)==0):
        userInput = input("You currently dont have any conditions, Press A to add, or X to go back")
    else:
        print("Here are your current buy conditions : ")
        for condition in currentStradegy.buyConditions:
            print(condition.stringVersion)
        userInput = input("Enter the condition number to make changes to it. Or press a to add condition, or press x to exit")
    userInput = userInput.capitalize()

    if userInput=="A":
        currentStradegy.addBuyCondition(addCondition())
    

def changeSellCondition(currentStradegy):
    userInput = None
    if (len(currentStradegy.sellConditions)==0):
        userInput = input("You currently dont have any conditions, Press A to add, or X to go back")
    else:
        print("Here are your current buy conditions : ")
        for condition in currentStradegy.sellConditions:
            print(condition.stringVersion)
        userInput = input("Enter the condition number to make changes to it. Or press a to add condition, or press x to exit")
    userInput = userInput.capitalize()

    if userInput=="A":
        currentStradegy.addSellCondition(addCondition())


def createStradegy():
    stradegyName = input("What is this stradegy going to be called?")
    currentStradegy = Stradegy(stradegyName)
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
        changeSellCondition(currentStradegy)
    elif (userInput == "b"):
        changeBuyCondition(currentStradegy)
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

