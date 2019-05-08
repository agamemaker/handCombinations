from handLogic import timeTestIterative, timeTestRecursive, timeTestRecursiveBoolean
from makeHands import makeHands
import time

def main():
    totalCount = 0
    successCount = 0
    hands = makeHands(5)
    startTime = time.time()
    for hand in hands:
        totalCount += 1
        if timeTestIterative(hand):
            successCount += 1
    iterativeTime = time.time()
    print("Iterative")
    print(iterativeTime - startTime)
    print(totalCount)
    print(successCount)
    totalCount = 0
    successCount = 0
    hands = makeHands(5)
    startTime = time.time()
    for hand in hands:
        totalCount += 1
        if timeTestRecursive(hand):
            successCount += 1
    recursiveTime = time.time()
    print("Iterative")
    print(recursiveTime - startTime)
    print(totalCount)
    print(successCount)
    totalCount = 0
    successCount = 0
    hands = makeHands(5)
    startTime = time.time()
    for hand in hands:
        totalCount += 1
        if timeTestRecursiveBoolean(hand):
            successCount += 1
    booleanTime = time.time()
    print("Iterative")
    print(booleanTime - startTime)
    print(totalCount)
    print(successCount)
    totalCount = 0
    successCount = 0


if __name__ == "__main__":
    main()
