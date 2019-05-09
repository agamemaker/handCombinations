from handLogic import timeTestIterative, timeTestIterativeBoolean, timeTestRecursive, timeTestRecursiveBoolean, \
    straightBoolean, straightCount
from makeHands import makeHands
import time

def main():
    myfunc = timeTestIterative
    handSize = 5
    timeTest(handSize, straightCount, "Straight")
    timeTest(handSize, straightBoolean, "Straight Boolean")
    timeTest(handSize, timeTestIterative, "Iterative")
    timeTest(handSize, timeTestIterativeBoolean, "Iterative Boolean")
    timeTest(handSize, timeTestRecursive, "Recursive")
    timeTest(handSize, timeTestRecursiveBoolean, "Recursive Boolean")

def timeTest(handSize, myfunc, label):
    hands = makeHands(handSize)
    totalCount = 0
    successCount = 0
    startTime = time.time()
    for hand in hands:
        totalCount += 1
        if myfunc(hand):
            successCount += 1
    endTime = time.time()
    print(label)
    print(endTime - startTime)
    print(totalCount)
    print(successCount)

if __name__ == "__main__":
    main()