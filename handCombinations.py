from itertools import combinations

SIZE = "size"
FOREST = "Forest"
MOUNTAIN = "Mountain"
CHANCELOR = "Chancellor of the Tangle"
SIMIAN = "Simian Spirit Guide"
RITUAL = "Ritual"
CANTOR = "Wild Cantor"
WIN_CONDITION = "winCondition"
LAY_OF_THE_LAND = "layOfTheLand"
RENEGADE_MAP = "Renegade Map"
FAITHLESS_LOOTING = "Faithless Looting"
MANAMORPHOSE = "Manamorphose"
WRAITH = "Street Wraith"
REFORGE = "Reforge the Soul"
PACT = "Pact of Negation"
SIDEBOARD = "sideboard"

def contains(hand, *cards):
    total = int(0)
    for card in cards:
        total += hand.count(card)
    return total

def ifFirstTurnGreenMana(hand):
    if FOREST in hand or CHANCELOR in hand:
        return True
    if CANTOR in hand and (MOUNTAIN in hand or SIMIAN in hand):
        return True
    if contains(hand, MOUNTAIN, SIMIAN) >= 2 and MANAMORPHOSE in hand:
        return True
    return False

def ifFirstTurnForest(hand):
    if ifFirstTurnGreenMana(hand) and (FOREST in hand or LAY_OF_THE_LAND):
        return True
    if MOUNTAIN in hand and RENEGADE_MAP in hand:
        return True
    return False

#not functional programing
def populateCatagory(cardMap, catagory, count):
    start = cardMap.get(SIZE)
    cardMap[catagory] = range(start, start + count)
    cardMap[SIZE] = start + count

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
    cardList += 4 * [FAITHLESS_LOOTING]
    cardList += 0 * [MANAMORPHOSE]
    cardList += 0 * [WRAITH]
    cardList += 2 * [REFORGE]
    cardList += 4 * [PACT]
    cardList += 0 * [SIDEBOARD]
    print(len(cardList))
    #print(cardList)
    return cardList

def makeHands(handSize):
    #return combinations(populateDeck(),handSize)
    return combinations(populate(),handSize)

def main():
    totalCount = 0
    successCount = 0
    hands = makeHands(7)
    for hand in hands:
        totalCount += 1
        if ifFirstTurnForest(hand) and (WIN_CONDITION in hand or FAITHLESS_LOOTING in hand) and contains(hand, FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP) >= 2:
            successCount += 1
    print(totalCount)
    print(successCount)


if __name__ == "__main__":
    main()
