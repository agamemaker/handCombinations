from constants import RECROSS, BELCHER, SHATTER, STRIKE, MANAMORPHOSE, FEAT, MOON, \
    handContains, handCount, REDMANA, GREENMANA, UNTAPPEDLAND, RITUAL2, LAND, hasFullPlunge, CSHIFTR, TITAN, PLUNGE, \
    DESPERATE


def isTurnTwoMoon(hand):
    if MOON not in hand:
        return False

    if handContains(REDMANA, hand) and handContains(UNTAPPEDLAND,hand) and handContains(RITUAL2, hand):
        return True
    if SHATTER in hand and STRIKE in hand and handCount(UNTAPPEDLAND, hand) >= 2:
        return True
    if handContains(GREENMANA, hand) and handContains(UNTAPPEDLAND,hand) and handContains(RITUAL2, hand) and MANAMORPHOSE in hand:
        return True
    if handContains(REDMANA, hand) and hasFullPlunge(hand):
        return True

    return False

def isTurnThree(hand):
    if len(hand) < 4:
        return False

    if isTurnThreeRecross(hand):
        return True

    if isTurnThreeBelcher(hand):
        return True

    return False

def isTurnThreeRecross(hand):
    if RECROSS not in hand:
        return False


    #turn 2 rit color shift
    if handContains(RITUAL2, hand) and handContains(CSHIFTR, hand) and \
            handCount(LAND, hand) >= 2 and handContains(UNTAPPEDLAND, hand) and handContains(REDMANA, hand):
        return True

    #turn 1 mana investment
    if handCount(UNTAPPEDLAND, hand) >= 2 and SHATTER in hand and STRIKE in hand:
        return True

    #Strike as second land
    if SHATTER in hand and STRIKE in hand and hand and handContains(RITUAL2, hand) and handCount(CSHIFTR, hand) >= 2:
        return True

    return False

def isTurnThreeBelcher(hand):
    if BELCHER not in hand:
        return False

    totalMana = 0
    ritMana = 0
    #land mana
    untapped = min(3, handCount(UNTAPPEDLAND, hand))
    lands = min(3, handCount(LAND, hand))
    landMana = [0,2,3,3]
    tapped = lands - untapped

    if tapped == 0:
        totalMana -= 1
        if(SHATTER in hand and STRIKE in hand):
            ritMana += 1

    ritMana += handCount(RITUAL2, hand)
    if(handCount(DESPERATE, hand) >= 2):
        ritMana += 1
    if(TITAN in hand and PLUNGE in hand):
        ritMana += 2
    if(FEAT in hand and ritMana > 0):
        ritMana += 3

    totalMana += untapped + landMana[lands] + ritMana

    if(totalMana >= 7 and handContains(REDMANA, hand)):
        return True
    else:
        return False