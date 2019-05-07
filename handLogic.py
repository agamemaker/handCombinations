from constants import FOREST, MOUNTAIN, CHANCELOR, SIMIAN, CANTOR, WIN_CONDITION, LAY_OF_THE_LAND, RENEGADE_MAP, \
    FAITHLESS_LOOTING, MANAMORPHOSE


def contains(hand, *cards):
    total = int(0)
    for card in cards:
        total += hand.count(card)
    return total


def ifplayable(hand):
    return ifFirstTurnForest(hand) and (WIN_CONDITION in hand or FAITHLESS_LOOTING in hand) and contains(hand, FOREST, MOUNTAIN, LAY_OF_THE_LAND, RENEGADE_MAP) >= 2


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