from Stradegy import Stradegy

stradegyList = []
game = True

print("Welcome to the Stock Analyzer program!")
print(" ")

def changeBuyCondition(currentStradegy):
    print("Here are your current buy conditions : ")
    for condition in currentStradegy.sellConditions:
        print(condition.stringVersion)

def changeSellCondition(currentStradegy):
    print("Here are your current sell conditions : ")
    for condition in currentStradegy.sellConditions:
        print(condition.stringVersion)


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

