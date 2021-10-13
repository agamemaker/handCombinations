import csv
import random
from itertools import combinations
from math import floor

from constants import SWAMP, FOREST, MOUNTAIN, SHATTER, MAULING, \
    DOMINANCE, STRIKE, SONG, SEAGATE, SPIKE, FEAT, VALAKUT
from handLogic.belcherHL import isTurnTwoMoon, isTurnThree
from handLogic.handLogic import isPowderable, isPlayableAtSize, scoreHand, isTurnThreeSalvage, isTurnOneSalvage
from makeHands import makeHands, populateDeck, populateDecklist

verbose = True
sampleSize = 10000
fullCombination = False
csvoutput = True

def combinationBaseHands(file):
    totalCount = 0
    successArray = [0]*16

    hands = makeHands(7, file)
    for hand in hands:
        totalCount += 1
        if totalCount%1000000 == 0:
            print(totalCount)
        index = scoreHand(hand)
        successArray[index] += 1
    for i in successArray:
        print(i/totalCount)

def combinationBaseHandsSpy(file):
    totalCount = 0
    success = 0

    hands = makeHands(7, file)
    for hand in hands:
        totalCount += 1
        if totalCount%10000000 == 0:
            print(totalCount)
        if isTurnOneSalvage(hand):
            success += 1
    print(success)
    print(totalCount)
    print(success/totalCount)

def sampleBasedHands(decklist):
    sampleSize = 1000000
    deck = populateDeck(decklist)
    handPercentages = sampleHands(deck, sampleSize)
    print(handPercentages)

def sampleHands(deck, sampleSize):
    handSizes = [0]*8
    random.seed(0)
    for i in range(sampleSize):
        handSize = findKeepableHand(deck)
        handSizes[handSize] += 1
    handPercentages = []
    for size in handSizes:
        handPercentages += [size / sampleSize]
    return handPercentages

def findKeepableHand(deck):
    handSize = 7
    hand = random.sample(deck, 7)
    removed = []
    searchableLands = deck.count(FOREST) + deck.count(MOUNTAIN) + deck.count(SWAMP)
    while handSize > 0:
        #print(hand)
        if isPlayableAtSize(hand, handSize):
            break
        tempDeck = isPowderable(deck[:], removed, hand)
        if tempDeck:
            deck = tempDeck
            hand = random.sample(deck, handSize)
        else:
            handSize -= 1
            hand = random.sample(deck, 7)
    return handSize

def sampleBasedScores(decklist):
    successArray = [0]*16
    sampleSize = 1000000
    deck = populateDeck(decklist)
    random.seed(0)
    for i in range(sampleSize):
        hand = random.sample(deck, 7)
        successArray[scoreHand(hand)] += 1
    for i in successArray:
        print(i/sampleSize)

def newsampleBasedHands(decklist, test):
    sampleSize = 1000000
    deck = populateDeck(decklist)
    handPercentages = newsampleHands(deck, sampleSize, test)
    print(handPercentages)

def newsampleHands(deck, sampleSize, test):
    handSizes = [0]*8
    random.seed(0)

    for i in range(sampleSize):
        handSize = newfindKeepableHand(deck, test, random)
        handSizes[handSize] += 1

    handPercentages = []
    for size in handSizes:
        handPercentages += [size / sampleSize]
    return handPercentages



def newfindKeepableHand(deck, test, random):
    handSize = 7
    while handSize > 0:
        baseHand = random.sample(deck, 7)
        possibleHands = combinations(baseHand, handSize)
        for hand in possibleHands:
            hands = []
            if test(hand):
                hands += [hand]
            if hands:
                return handSize
        handSize -= 1
    return 0

def tuning(decklist, test, tuneAbleCards):
    deck = populateDeck(decklist)
    oldBestRate = newsampleHands(deck, sampleSize, test)[0]
    while(True):
        failrates = []
        for cardIn in tuneAbleCards:
            for cardOut in tuneAbleCards:
                match = cardIn == cardOut
                tooMany = deck.count(cardIn) >= 4
                tooFew = deck.count(cardOut) <= 0
                if match or tooMany or tooFew:
                    failrates += [1]
                else:
                    testDeck = deck[:]
                    testDeck.append(cardIn)
                    testDeck.remove(cardOut)
                    testDeck.sort()
                    handPercentages = newsampleHands(testDeck, sampleSize, test)
                    failrates += [handPercentages[0]]
                    if verbose:
                        #print(cardIn + " for " + cardOut)
                        print("+" + cardIn + " -" + cardOut)
                        print(handPercentages)

        if verbose:
            print(failrates)
        bestRate = min(failrates)
        if bestRate >= oldBestRate:
            break
        else:
            oldBestRate = bestRate
            bestIndex = failrates.index(bestRate)
            across = len(tuneAbleCards)
            cardIn = tuneAbleCards[floor(bestIndex/across)]
            cardOut = tuneAbleCards[bestIndex%across]
            print("+" + cardIn + " -" + cardOut)
            deck.append(cardIn)
            deck.remove(cardOut)
            deck.sort()
    fileSplit = decklist.split(".",1)
    writeFilename = fileSplit[0] + "_tuned." + fileSplit[1]
    populateDecklist(deck, writeFilename)
    if verbose:
        for card in deck:
            print(card)

def noMullTest(decklist, test):
    deck = populateDeck(decklist)
    totalCount = 0
    success = 0
    testPass = False
    #hands
    hands =[]
    if fullCombination:
        hands = makeHands(7, decklist)
    else:
        random.seed(0)
        for i in range(sampleSize):
            hands += [random.sample(deck, 7)]

    #testing
    with open('turn3.csv', mode='w') as csvFile:
        writer = csv.writer(csvFile)
        for hand in hands:
            totalCount += 1
            testPass = test(hand)
            if totalCount % 10000000 == 0 and verbose:
                print(totalCount)
            if testPass:
                success += 1
            if csvoutput:
                writer.writerow([testPass]+hand)

    print(success)
    print(totalCount)
    print(success / totalCount)


if __name__ == "__main__":
    #tuning("decklists/salvage_spy.txt", isTurnThreeSalvage, [SHATTER, MAULING, DOMINANCE])
    tuning("decklists/belcher.txt", isTurnThree, [STRIKE, VALAKUT, SEAGATE, FEAT])
    #noMullTest("decklists/belcher.txt", isTurnThree)
    noMullTest("decklists/tuned.txt", isTurnThree)
    #noMullTest("decklists/salvage_spy.txt", isTurnThreeSalvage)