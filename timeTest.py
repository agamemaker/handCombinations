from handLogic import timeTestIterative, timeTestIterativeBoolean, timeTestRecursive, timeTestRecursiveBoolean
from makeHands import makeHands
import time

def main():
    iterativeTest()
    iterativeBoolTest()
    recursiveTest()
    recursiveBoolTest()

def iterativeTest():
    hands = makeHands(4)
    startTime = time.time()
    totalCount = 0
    successCount = 0
    for hand in hands:
        totalCount += 1
        if timeTestIterative(hand):
            successCount += 1
    print(totalCount)
    print(successCount)
    endTime = time.time()
    print("Iterative")
    print(endTime - startTime)

def iterativeBoolTest():
    hands = makeHands(4)
    startTime = time.time()
    totalCount = 0
    successCount = 0
    for hand in hands:
        totalCount += 1
        if timeTestIterativeBoolean(hand):
            successCount += 1
    print(totalCount)
    print(successCount)
    endTime = time.time()
    print("Iterative Boolean")
    print(endTime - startTime)

def recursiveTest():
    hands = makeHands(4)
    startTime = time.time()
    totalCount = 0
    successCount = 0
    for hand in hands:
        totalCount += 1
        if timeTestRecursive(hand):
            successCount += 1
    print(totalCount)
    print(successCount)
    endTime = time.time()
    print("Recursive")
    print(endTime - startTime)

def recursiveBoolTest():
    hands = makeHands(4)
    startTime = time.time()
    totalCount = 0
    successCount = 0
    for hand in hands:
        totalCount += 1
        if timeTestRecursiveBoolean(hand):
            successCount += 1
    print(totalCount)
    print(successCount)
    endTime = time.time()
    print("Recursive Boolean")
    print(endTime - startTime)


if __name__ == "__main__":
    main()
