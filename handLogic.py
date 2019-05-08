import time

from constants import FOREST, MOUNTAIN, CHANCELOR, SIMIAN, CANTOR, WIN_CONDITION, LAY_OF_THE_LAND, RENEGADE_MAP, \
    LOOTING, MANAMORPHOSE

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def recursivecontains(self, cards):
        total = int(0)
        if isinstance(cards, list):
            for card in cards:
                total += recursivecontains(self.cards, card)
        else:
            total += self.cards.count(cards)
        return total

def contains(hand, *cards):
    total = int(0)
    for card in cards:
        total += hand.count(card)
    return total

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

def ifplayable(hand):
    return ifFirstTurnForest(hand) and (WIN_CONDITION in hand or LOOTING in hand) and contains(hand, FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP) >= 2

#testing
def timeTestRecursive(hand):
    return recursivecontains(hand, [FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP])

def timeTestIterative(hand):
    return contains(hand, FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP)

def timeTestRecursiveBoolean(hand):
    return recursiveIn(hand, [FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP])

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