from itertools import combinations

def populateDeck(file):
    cardList = []
    deckFile = open(file)
    for line in deckFile:
        splitLine = line.rstrip().split(" ",1)
        #print(splitLine)
        cardList += int(splitLine[0]) * [splitLine[1]]
    deckFile.close()
    print(len(cardList))
    return cardList


def makeHands(handSize, file):
    return combinations(populateDeck(file),handSize)