from itertools import combinations

from constants import FOREST, MOUNTAIN, CHANCELOR, SIMIAN, RITUAL, CANTOR, WIN_CONDITION, LAY_OF_THE_LAND, RENEGADE_MAP, \
    LOOTING, MANAMORPHOSE, WRAITH, REFORGE, PACT, SIDEBOARD


def populateDeck():
    cardList = []
    deckFile = open("decklist.txt")
    for line in deckFile:
        splitLine = line.rstrip().split(" ",1)
        print(splitLine)
        cardList += int(splitLine[0]) * [splitLine[1]]
    deckFile.close()
    print(len(cardList))
    return cardList


def populate():
    cardList = []
    cardList += 2 * [FOREST]
    cardList += 2 * [MOUNTAIN]
    cardList += 4 * [CHANCELOR]
    cardList += 4 * [SIMIAN]
    cardList += 8 * [RITUAL]
    cardList += 4 * [CANTOR]
    cardList += 8 * [WIN_CONDITION]
    cardList += 14 * [LAY_OF_THE_LAND]
    cardList += 4 * [RENEGADE_MAP]
    cardList += 4 * [LOOTING]
    cardList += 0 * [MANAMORPHOSE]
    cardList += 0 * [WRAITH]
    cardList += 2 * [REFORGE]
    cardList += 4 * [PACT]
    cardList += 0 * [SIDEBOARD]
    print(len(cardList))
    return cardList


def makeHands(handSize):
    #return combinations(populateDeck(),handSize)
    return combinations(populate(),handSize)