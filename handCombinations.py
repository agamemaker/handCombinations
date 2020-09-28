import csv
import random
from itertools import combinations
from math import floor

from constants import SWAMP, FOREST, MOUNTAIN, EMERIA, PELAKKA, TALISMAN, SHATTER, SPHERE, SEAGATE, TANGLED, MAULING
from handLogic import isPowderable, isPlayableAtSize, scoreHand, isTunrThreeSVOAS
from makeHands import makeHands, populateDeck

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
    sampleSize = 10000
    deck = populateDeck(decklist)
    handPercentages = newsampleHands(deck, sampleSize, test)
    print(handPercentages)

def newsampleHands(deck, sampleSize, test):
    handSizes = [0]*8
    random.seed(0)

    for i in range(sampleSize):
        handSize = newfindKeepableHand(deck, test)
        handSizes[handSize] += 1

    handPercentages = []
    for size in handSizes:
        handPercentages += [size / sampleSize]
    return handPercentages



def newfindKeepableHand(deck, test):
    handSize = 7
    while handSize > 0:
        baseHand = random.sample(deck, 7)
        possibleHands = combinations(baseHand, handSize)
        for hand in possibleHands:
            if test(hand):
                with open('turn3.csv', mode='a') as turn3win:
                    winWriter = csv.writer(turn3win)
                    winWriter.writerow([handSize]+baseHand)
                return handSize
        with open('turn3no.csv', mode='a') as turn3no:
            noWriter = csv.writer(turn3no)
            noWriter.writerow([handSize] + baseHand)
        handSize -= 1
    return 0

def tuning(decklist, test, tuneAbleCards):
    sampleSize = 10000
    deck = populateDeck(decklist)
    oldBestRate = 1
    while(True):
        failrates = []
        for cardIn in tuneAbleCards:
            for cardOut in tuneAbleCards:
                if cardIn == cardOut or deck.count(cardIn) >= 4 or deck.count(cardOut) <= 0:
                    failrates += [1]
                else:
                    print(cardIn + " " + cardOut)
                    testDeck = deck[:]
                    testDeck.append(cardIn)
                    testDeck.remove(cardOut)
                    testDeck.sort()
                    #print(testDeck)
                    handPercentages = newsampleHands(testDeck, sampleSize, test)
                    failrates += [handPercentages[0]]
        print(failrates)
        bestRate = min(failrates)
        if bestRate >= oldBestRate:
            break
        else:
            oldBestRate = bestRate
            bestIndex = failrates.index(bestRate)
            across = len(tuneAbleCards)
            print(bestIndex)
            cardIn = tuneAbleCards[floor(bestIndex/across)]
            cardOut = tuneAbleCards[bestIndex%across]
            print("+" + cardIn + " -" + cardOut)
            deck.append(cardIn)
            deck.remove(cardOut)
            deck.sort()
        #print(deck)
    for card in deck:
        print(card)


if __name__ == "__main__":
    #combinationBaseHands("decklists/mike.txt")
    #sampleBasedScores("decklists/GB_decklist.txt")
    #sampleBasedHands("decklists/GB_decklist.txt")
    newsampleBasedHands("decklists/sundering_dredge.txt", isTunrThreeSVOAS)
    #tuning("decklists/sundering_dredge.txt", isTunrThreeSVOAS, [SHATTER, PELAKKA, SPHERE, EMERIA, SEAGATE, MAULING, TANGLED, TALISMAN])