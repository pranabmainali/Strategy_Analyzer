import Stradegy

stradegyList = []
game = True

print("Welcome to the Stock Analyzer program!")
print(" ")

def createStradegy():
    stradegyName = input("What is this stradegy going to be called?")
    currentStradegy = Stradegy(stradegyName)
    stock = input("Please enter your stock's ticker symbol . Example (MSFT)")
    stock = stock.capitalize()
    interval = input("Please input the interval in which you want your data. One of (5m, 15m, 30m, 1h, 1d, 1wk, 1mo, 3mo)")
    maiximumCoverageDate = currentStradegy.addStock(stock, interval)
    print("Please note that only data as far back as "+maiximumCoverageDate+" can be tested on!")
    


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

