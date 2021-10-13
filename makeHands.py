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

def populateDecklist(deck, file):
    dictDeck = {}
    for card in deck:
        if card in dictDeck.keys():
            dictDeck[card] += 1
        else:
            dictDeck[card] = 1

    print(dictDeck)
    deckFile = open(file,"w")
    for card in dictDeck:
        line = str(dictDeck[card]) + " " + card +"\n"
        print(line)
        deckFile.write(line)
    deckFile.close()