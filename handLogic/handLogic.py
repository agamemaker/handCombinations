import time
from itertools import combinations

from constants import FOREST, MOUNTAIN, CHANCELOR, SIMIAN, CANTOR, LAY_OF_THE_LAND, MAP, \
    MANAMORPHOSE, ATTUNE, CARAVAN, OPEN, TRAVERSE, BELCHER, RECROSS, SWAMP, SPY, UNDERCITY, PENTAD, \
    TALISMAN, PYRETIC, DESPERATE, TIMBER, POWDER, ORACLE, JOURNEY, REFORGE, UNEARTH, BALA, VALAKUT, FEAT, AGADEEM, \
    PELAKKA, EMERIA, SEAGATE, SHATTER, SPHERE, MAULING, TANGLE, DOMINANCE, INTERACTION


def isplayable(hand):
    return containsFirstTurnGreenMana(hand) and hasWinConditionOrDrawEngine(hand) and containsTwoPotentialLands(hand) \
           and containsFirstTurnLand(hand)

def containsFirstTurnGreenMana(hand):
    #Straight genrate green mana
    if FOREST in hand or CHANCELOR in hand or TIMBER in hand:
        return True
    #cantor filtering
    if CANTOR in hand and (MOUNTAIN in hand or SIMIAN in hand):
        return True
    #offland and map
    if MOUNTAIN in hand or SWAMP in hand and MAP in hand:
        return True
    #manamorphose
    if MANAMORPHOSE in hand and (hand.count(MOUNTAIN) + hand.count(SIMIAN)) >= 1 and (hand.count(MOUNTAIN) + \
        hand.count(SIMIAN) + hand.count(SWAMP)) >= 2:
        return True
    #pentad Prism
    if PENTAD in hand and SWAMP in hand and (hand.count(MOUNTAIN) + hand.count(SIMIAN)) >= 1:
        return True
    #talisman
    if TALISMAN in hand and (hand.count(MOUNTAIN) + hand.count(SIMIAN) + hand.count(SWAMP)) >= 2:
        return True
    return False

def hasWinConditionOrDrawEngine(hand):
    return BELCHER in hand or RECROSS in hand or UNDERCITY in hand or SPY in hand

def containsTwoPotentialLands(hand):
    return possibleBasics(hand) >= 2


def possibleBasics(hand):
    return hand.count(FOREST) + hand.count(MOUNTAIN) + hand.count(LAY_OF_THE_LAND) + hand.count(ATTUNE) + \
            hand.count(CARAVAN) + hand.count(OPEN) + hand.count(TRAVERSE) + hand.count(MAP) + \
            hand.count(SWAMP)

def additionalMana(hand):
    return hand.count(FOREST) + hand.count(MOUNTAIN) + hand.count(SWAMP) + hand.count(PYRETIC) + hand.count(DESPERATE) + \
           hand.count(SIMIAN) + hand.count(CHANCELOR)

def containsFirstTurnLand(hand):
    return (hand.count(FOREST) + hand.count(MOUNTAIN) + hand.count(LAY_OF_THE_LAND) + hand.count(ATTUNE) + \
            hand.count(CARAVAN) + hand.count(OPEN) + hand.count(TRAVERSE) + hand.count(SWAMP)) >= 1

def containsFlexible(hand, *cards):
    total = int(0)
    for card in cards:
        if isinstance(card, list):
            for induvidual in card:
                total += hand.count(card)
        else:
            total += hand.count(card)
    return total

def contains(hand, *cards):
    total = int(0)
    for card in cards:
        total += hand.count(card)
    return total

def iterativeInFlexible(hand, *cards):
    for card in cards:
        if isinstance(card, list):
            for induvidual in card:
                if induvidual in hand:
                    return True
        else:
            if card in hand:
                return True
    return False

def iterativeIn(hand, *cards):
    total = int(0)
    for card in cards:
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


def isPowderable(deck, removed, hand):
    for card in hand:
        deck.remove(card)
    removed += hand
    #no powder
    if POWDER not in hand:
        return []
    #cannot bin land or combo
    if FOREST in hand or MOUNTAIN in hand or SWAMP in hand or ORACLE in hand:
        return []
    #too many journeys or reforge
    if (JOURNEY not in deck and JOURNEY in removed) or (REFORGE not in deck and REFORGE in removed):
        return []
    #can't combo
    if UNEARTH in removed and MANAMORPHOSE in hand:
        return []
    return deck


def isTurnWin(baseHand, handSize, searchableLands):
    possibleHands = combinations(baseHand, handSize)
    for hand in possibleHands:
        lands = min([searchableLands, possibleBasics(hand)]) + hand.count(BALA) + hand.count(VALAKUT)
        ritMana = additionalMana(hand)

        if FEAT in hand:
            ritMana += 3


def isPlayableAtSize(baseHand, handSize):
    possibleHands = combinations(baseHand,handSize)
    for hand in possibleHands:
        if handSize == 7 or handSize == 6:
            if scoreHand(hand) == 15:
                return True
        elif handSize == 5:
            if scoreHand(hand) >= 13:
                return True
        elif handSize <= 4:
            if scoreHand(hand) >=12:
                return True

def scoreHand(hand):
    index = 0
    if containsTwoPotentialLands(hand):
        index += 1
    if hasWinConditionOrDrawEngine(hand):
        index += 2
    if containsFirstTurnLand(hand):
        index += 4
    if containsFirstTurnGreenMana(hand):
        index += 8
    return index

def isTurnThreeSalvage(hand):
    if len(hand) < 4:
        return False

    #contains black mana
    if not(AGADEEM in hand or PELAKKA in hand or MAULING in hand or TALISMAN in hand or PENTAD in hand or SPHERE in hand or DOMINANCE in hand):
        return False

    #contains finisher
    if not(SPY in hand or UNDERCITY in hand or BELCHER in hand):
        return False

    if not hasFourManaTurnThree(hand):
        return False

    return True

def isTurnThreeAndInteraction(hand):
    if not isTurnThreeSalvage(hand):
        return False

    if not handContains(hand, INTERACTION):
        return False

    return True

def handContains(hand, containsL):
    for card in containsL:
        if card in hand:
            return True
    return False


def hasFourManaTurnThree(hand):
    untapLands = hand.count(EMERIA) + hand.count(SEAGATE) + hand.count(AGADEEM) + hand.count(SHATTER) + hand.count(
        TIMBER)
    tappedLands = hand.count(PELAKKA) + hand.count(TANGLE) + hand.count(MAULING)
    neededTapped = min(max(3 - untapLands, 0), tappedLands)
    totalLands = min(untapLands + tappedLands, 3)
    manaFromLands = 0
    for i in range(1, 4):
        manaFromLands += min(i, totalLands)
    totalMana = manaFromLands - neededTapped + hand.count(SIMIAN)

    # contains accelerant and proper lands
    if PENTAD in hand and totalMana >= 4 and baseColors(hand) >= 2:
        return True
    if (TALISMAN in hand or SPHERE in hand or DOMINANCE in hand) and totalLands >= 3 and untapLands >= 2:
        return True
    if (TALISMAN in hand or SPHERE in hand or DOMINANCE in hand) and totalLands >= 2 and untapLands >= 1 and SIMIAN in hand:
        return True
    if totalLands + hand.count(SIMIAN) >= 4 and untapLands >= 1:
        return True
    return False


def baseColors(hand):
    colors = 0
    if EMERIA in hand:
        colors += 1
    if SEAGATE in hand:
        colors += 1
    if AGADEEM in hand or PELAKKA in hand or MAULING in hand:
        colors += 1
    if SHATTER in hand or SIMIAN in hand:
        colors += 1
    if TIMBER in hand or TANGLE in hand:
        colors += 1
    return colors

def isTurnOneSalvage(hand):
    if hand.count(SIMIAN) >= 3 and (SPY in hand or UNDERCITY in hand):
        if AGADEEM in hand:
            return True
        elif PENTAD in hand and (EMERIA in hand or SEAGATE in hand or TIMBER in hand):
            return True

    if hand.count(SIMIAN) >= 4 and TALISMAN in hand and (SPY in hand or UNDERCITY in hand):
        if EMERIA in hand or SEAGATE in hand or AGADEEM in hand or SHATTER in hand or TIMBER in hand:
            return True
    return False