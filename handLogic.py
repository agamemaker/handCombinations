import time

from constants import FOREST, MOUNTAIN, CHANCELOR, SIMIAN, CANTOR, WIN_CONDITION, LAY_OF_THE_LAND, RENEGADE_MAP, \
    LOOTING, MANAMORPHOSE

def contains(hand, *cards):
    total = int(0)
    for card in cards:
        if isinstance(card, list):
            for induvidual in card:
                total += hand.count(card)
        else:
            total += hand.count(card)
    return total

def iterativeIn(hand, *cards):
    for card in cards:
        if isinstance(card, list):
            for induvidual in card:
                if induvidual in hand:
                    return True
        else:
            if card in hand:
                return True
    return False

def recursivecontains(hand, cards):
    total = int(0)
    if isinstance(cards, list):
        for card in cards:
            total += recursivecontains(hand, card)
    else:
        total += hand.count(cards)
    return total

def recursiveIn(hand, cards):
    total = int(0)
    if isinstance(cards, list):
        for card in cards:
            if recursivecontains(hand, card):
                return True
    else:
        if cards in hand:
            return True
    return False


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

def ifplayable(hand):
    return ifFirstTurnForest(hand) and (WIN_CONDITION in hand or LOOTING in hand) and contains(hand, FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP) >= 2

#testing
def straightCount(hand):
    return stackTestCount(hand)


def stackTestCount(hand):
    return hand.count(FOREST) + hand.count(MOUNTAIN) + hand.count(LAY_OF_THE_LAND) + hand.count(RENEGADE_MAP)


def straightBoolean(hand):
    return stackTestBool(hand)


def stackTestBool(hand):
    return FOREST in hand or MOUNTAIN in hand or LAY_OF_THE_LAND in hand or RENEGADE_MAP in hand


def timeTestIterative(hand):
    return contains(hand, FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP)

def timeTestIterativeBoolean(hand):
    return iterativeIn(hand, [FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP])

def timeTestRecursive(hand):
    return recursivecontains(hand, [FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP])

def timeTestRecursiveBoolean(hand):
    return recursiveIn(hand, [FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP])