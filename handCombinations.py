from handLogic import ifplayable
from makeHands import makeHands

def main():
    #totalCount = 0
    successCount = 0
    hands = makeHands(7)
    for hand in hands:
        #totalCount += 1
        if ifplayable(hand):
            successCount += 1
    #print(totalCount)
    print(successCount)


if __name__ == "__main__":
    main()
