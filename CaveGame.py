import random

health = 50
sanity = 100
steps = 0
rounds = 0
inventoryList = []
gameEnded = False

#Tecnichan mysc. functions

def printAndPressEnter(text):
    print(text)
    input()

def getInput():
    while True:
        userChoice = input()
        if userChoice != (''):
            return int(userChoice)
        else:
            print("Please enter a number")

#Main functions

def main():
    introText()
    while True:
        checkIfGameEnded()
        if gameEnded:
            break
        else:
            mainMenu()

def mainMenu():
    printStats()
    print("""
    1) Walk Forward
    2) Rest
    3) Inventory
    4) Exit Game
    """)
    while True:
        match getInput():
            case 1:
                takeStep()
                break
            case 2:
                takeRest()
                break
            case 3:
                openInventory()
                break
            case 4:
                exitGameEnding()
                break
            case _:
                print("Not an option; Please pick again")

def printStats():
    global health
    global sanity
    global steps
    global rounds
    print("Health: {}/50   Sanity: {}/100   Steps taken: {}/50   Rounds spent: {}".format(health, sanity, steps, rounds))

def checkIfGameEnded():
    global health
    global sanity
    global steps
    global gameEnded

    if checkIfStatGone(health):
        lossOfHealthEnding()
        printFinalScore()
        gameEnded = True
    elif checkIfStatGone(sanity):
        lossOfSanityEnding()
        printFinalScore()
        gameEnded = True
    elif steps >= 50:
        trueEnding()
        printFinalScore()
        gameEnded = True

#Action functions

def takeStep():
    global steps
    global sanity
    global rounds
    
    printAndPressEnter("You take a step forward")
    steps += 1
    generateRandEvent()
    sanityLoss = random.randint(5, 9)
    printAndPressEnter("You lose {} sanity from the caves".format(sanityLoss))
    sanity -= sanityLoss
    rounds += 1
    
def takeRest():
    global rounds

    generateRandSleepEvent()
    gainHealth(random.randint(10, 20))
    rounds += 1

#Stat related funttions

def checkIfStatGone(stat):
    if stat <= 0:
        return True
    else:
        return False

def gainHealth(healthGain):
    global health
    maxHealth = 50
    if (health + healthGain) > maxHealth:
        health = maxHealth
        printAndPressEnter("You maxxed your health")
    else:
        health += healthGain
        printAndPressEnter("You gained {} health".format(healthGain))

def gainSanity(sanityGain):
    global sanity
    maxSanity = 100
    if (sanity + sanityGain) > maxSanity:
        sanity = maxSanity
        printAndPressEnter("You maxxed your sanity")
    else:
        sanity += sanityGain
        printAndPressEnter("You gained {} sanity".format(sanityGain))

#Inventory related functions 

def openInventory():
    printInventory()
    selectInventoryItem()

def printInventory():
    global inventoryList
    goBackIndex = (len(inventoryList) + 1)

    print("Inventory:")
    if len(inventoryList) > 0:
        for i in range (1, (len(inventoryList) + 1)):
            print("    {}) {}".format(str(i), inventoryList[i - 1]))
    else:
        print("    There is nothing in here...")
    print("    {}) Nevermind".format(str(goBackIndex)))    

def selectInventoryItem():
    global inventoryList

    while True:
        selectedItemIndex = getInput()
        if selectedItemIndex == (len(inventoryList) + 1):
            break
        elif selectedItemIndex <= len(inventoryList):
            interactWithInventoryItem(selectedItemIndex - 1)
            break
        else:
            print("Not an option; Please pick again")    

def interactWithInventoryItem(itemIndex):
    global inventoryList
    item = inventoryList[itemIndex]
    global rounds
    print("""
    1) Use item
    2) Throw item away
    3) Nevermind
    """)
    while True:
        match getInput():
            case 1:
                useItem(item)
                del inventoryList[itemIndex]
                rounds += 1
                break
            case 2:
                print("You threw away: " + item)
                del inventoryList[itemIndex]
                rounds += 1
                break
            case 3:
                break
            case _:
                print("Not an option; Please pick again")

def addItemToInventory(item):
    global inventoryList
    if len(inventoryList) >= 9:
        replaceInventoryItem(item)
    else:
        printAndPressEnter("You added {} to your inventory".format(item))
        inventoryList.append(item)

def replaceInventoryItem(newItem):
    printAndPressEnter("Your inventory is full; You may replace an item you have for {} or forget it")

    printInventory()
    global inventoryList

    while True:
        selectedItemIndex = getInput()
        if selectedItemIndex == (len(inventoryList) + 1):
            print("You didn't replace anthing and dropped {}".format(newItem))
            break
        elif selectedItemIndex <= len(inventoryList):
            print("You dropped {} and replaced it with {}".format(inventoryList[selectedItemIndex - 1], newItem))
            del inventoryList[selectedItemIndex - 1]
            inventoryList.append(newItem)
            break
        else:
            print("Not an option; Please pick again")  

#Using an item function

def useItem(item):
    printAndPressEnter("You used: " + item)
    match item:
        case "Strange Muchrooms":
            gainSanity(55)
        case "Stale Old Bread":
            gainHealth(20)

#Event related functions

def generateRandEvent(): 
    match random.randint(1, 7):
        case 1:
            findItem()
        case 2:
            findShortcut()
        case 3:
            trip()
        case 4:
            getLost()
        case 5:
            schizophrenia()
        case _:
            printAndPressEnter("You keep going normally")

def findItem():
    item = getRandItem()
    print("You found {}; Would you can add this to your inventory".format(item))
    print("""
    1) Add to inventory
    2) Drop it
    """)
    while True:
        match getInput():
            case 1:
                addItemToInventory(item)
                break
            case 2:
                print("You dropped {}".format(item))
                break
            case _:
                print("Not an option; Please pick again")

def getRandItem():
    match random.randint(1, 2):
        case 1:
            return "Strange Muchrooms"
        case 2:
            return "Stale Old Bread"

def findShortcut():
    global steps
    extraSteps = random.randint(3, 8)
    printAndPressEnter("You find so strange writings on the wall")
    printAndPressEnter("After further inspection, it appears that you found a secret shortcut")
    printAndPressEnter("You decide to follow it...")
    printAndPressEnter("You come out back to the main path, appearing to save {} steps".format(extraSteps))
    steps += extraSteps

def trip():
    global health
    damage = random.randint(7, 18)
    printAndPressEnter("As you take the next step, you accidentaly trip on something")
    printAndPressEnter("You take damage and lose {} health".format(damage))
    health -= damage

def getLost():
    global steps
    stepsLost = random.randint(5, 9)
    if stepsLost > steps:
        stepsLost = steps
    printAndPressEnter("It appears that you took a wrong turn somewhere")
    printAndPressEnter("Anthough you have a pretty clear path, you still managed to get lost")
    printAndPressEnter("You found your way back to the main path, but you lost about {} steps".format(stepsLost))
    steps -= stepsLost

def schizophrenia():
    global sanity
    sanityLoss = random.randint(8, 21)
    printAndPressEnter("You take your step as usual, until you spot something strange in the distance...")
    printAndPressEnter("It is strange; You believe it to be some sort of creature, but you can't quite define its features")
    printAndPressEnter("However, you blink, and what you were looking at seems to be gone")
    printAndPressEnter("You lost {} sanity".format(sanityLoss))
    sanity -= sanityLoss

#Sleep event functions

def generateRandSleepEvent():
    match random.randint(1, 6):
        case 1:
            haveNightmare()
        case _:
            printAndPressEnter("You have an average rest")
            gainSanity(random.randint(6, 17))

def haveNightmare():
    global sanity
    sanityLoss = random.randint(7, 19)
    printAndPressEnter("You seem to have a strange nightmare...")
    printAndPressEnter("You see queer shadows and strange creatures")
    printAndPressEnter("You lose {} sanity from this nightmare".format(sanityLoss))
    sanity -= sanityLoss

#Intro/Ending related functions

def introText():
    printAndPressEnter("You wake up in a strange cave")
    printAndPressEnter("You have seem to have no memory or idea of how you got here")
    printAndPressEnter("All you know is that you must escape")
    printAndPressEnter("You see a dimly-lit path in front of you")
    printAndPressEnter("All you can do is follow it")

def exitGameEnding():
    global gameEnded 
    gameEnded = True
    printAndPressEnter("After contemplating your time in the cave, you have decided that life isn't worth the effort of escaping")
    printAndPressEnter("You take the sharpest rock you can find and you kill yourself with it")
    print("Ending: You gave up")

def lossOfHealthEnding():
    printAndPressEnter("You have colected way too many wounds while in this cave")
    printAndPressEnter("All you efforts of survival have been useless, as now you lay in this dark cave...")
    printAndPressEnter("...Bleeding out...")
    printAndPressEnter("...And still trapped")
    print("Ending: You failed to live")

def lossOfSanityEnding():
    printAndPressEnter("You have spend a lot of time in this cave...")
    printAndPressEnter("...A little too much time")
    printAndPressEnter("Something about this cave has made you lose the last of your humanity")
    printAndPressEnter("The loss of your sanity consumes you...")
    printAndPressEnter("... And you get consumed by the shadows")
    print("Ending: You went insane")

def trueEnding():
    printAndPressEnter("You did it...")
    printAndPressEnter("After a long journey in this mysterious cave...")
    printAndPressEnter("You've finally made it out!")
    printAndPressEnter("...")
    printAndPressEnter("...But what now what?")
    print("Ending: You've made it?")

def printFinalScore():
    global steps
    global rounds
    print("Score: {} Steps; {} Rounds".format(steps, rounds))

#Just calls main so this whole thing can run
main()