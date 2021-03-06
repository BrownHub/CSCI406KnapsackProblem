# KnapsackProblem
# author: Kendall Brown

import time
import random
from copy import copy

def exhaustiveMethod(sackWeight, numberOfItems, items):

    # initialize values and run recursive method
    tempSet = list()
    powerSet = list()
    powerSet = generatePowerSet(items, tempSet, numberOfItems, powerSet)

    # examine power set for ideal value
    idealValue = 0
    reversedIdealLoad = list()
    currentLoad = list()
    for i in range(len(powerSet)):
        loadWeight = 0
        loadValue = 0
        currentLoad = copy(powerSet[i])
        # calculate wieght and value of each set
        for j in range(len(currentLoad)):
            loadWeight += currentLoad[j][0]
            loadValue += currentLoad[j][1]

        # check that set is not overweight and compare for greatest value
        if loadWeight <= sackWeight:
            if idealValue < loadValue:
                idealValue = loadValue
                reversedIdealLoad = copy(currentLoad)

    idealLoad = list()
    for i in range(len(reversedIdealLoad)):
        idealLoad.append(reversedIdealLoad[(len(reversedIdealLoad) - 1) - i])

    return idealLoad

def heuristicMethod(sackWeight, items):
    #sort items in descending order
    isSorted = False
    while not isSorted:
        isSorted = True

        for i in range(len(items)-1):
            first = items[i]
            second = items[i+1]
            firstRatio = first[1] / first[0]
            secondRatio = second[1] / second[0]

            # compare value to weight ratio of items
            if firstRatio < secondRatio:
                # swap items and run sort again after pass
                isSorted = False
                tempItem = first
                items[i] = second
                items[i+1] = tempItem
            elif firstRatio == secondRatio:
                # compare value of items
                if first[1] < second[1]:
                    # swap items and run sort again after pass
                    isSorted = False
                    tempItem = first
                    items[i] = second
                    items[i + 1] = tempItem

    #initialize values
    remainingWeight = sackWeight
    load = list()

    # add items until sack is full
    for i in range(len(items)):
        if remainingWeight - items[i][0] > 0:
            remainingWeight -= items[i][0]
            load.append(items[i])

    isSorted = False
    while not isSorted:
        isSorted = True

        for i in range(len(load) - 1):
            first = load[i]
            second = load[i + 1]

            # compare item numbers
            if first[2] > second[2]:
                # swap items and run sort again after pass
                isSorted = False
                tempItem = first
                load[i] = second
                load[i + 1] = tempItem

    return load

# referenced https://www.techiedelight.com/generate-power-set-given-set/
def generatePowerSet(items, tempSet, n, powerSet):

    # add to power set if all items have been considered
    if n == 0:
        setToAdd = copy(tempSet)
        powerSet.append(setToAdd)
        return powerSet

    # add nth element
    tempSet.append(items[n-1])
    powerSet = generatePowerSet(items, tempSet, n-1, powerSet)

    # don't add nth element
    tempSet.pop()
    powerSet = generatePowerSet(items, tempSet, n-1, powerSet)

    return powerSet

def randomGenerateData(n):
    knapsackWeight = int(200 * random.random() + 100)
    numItems = n

    with open("GeneratedData.txt", "w") as exhaustiveFile:
        exhaustiveFile.write("{}\n".format(knapsackWeight))
        exhaustiveFile.write("{}\n".format(numItems))

        for i in range(numItems):
            weight = int(80 * random.random() + 1)
            value = int(320 * random.random() + 30)
            exhaustiveFile.write("{} {}\n".format(weight, value))

if __name__ == '__main__':
    # ask to generate random data
    generateData = input("Generate data? - ")
    generateData = generateData.upper()

    while generateData != "Y" and generateData != "N":
        print("Try again")
        generateData = input("Generate data?\n:")

    if generateData == "Y":

        itemsToGenerate = int(input("How many items would you like to generate? - "))

        randomGenerateData(itemsToGenerate)


    # request method preference from user
    print("Choose a method:")
    print("E - Exhaustive")
    print("H - Heuristic")
    method = input("- ")
    method = method.upper()

    # check entry is appropriate
    while method != "E" and method != "H":
        print ("\n-Incorrect input-")
        print("Choose a method:")
        print("E - Exhaustive")
        print("H - Heuristic")
        method = input("- ")

    # request data file from user
    filename = input("Enter a file name: ")

    startTime = time.time()

    # read data from file
    with open(filename) as inputFile:
        sackWeight = int(inputFile.readline())
        numberOfItems = int(inputFile.readline())
        itemsFromFile = inputFile.read()

    # create items variable using data for the first item
    itemNumber = 1
    itemData = itemsFromFile.split()
    itemWeight = int(itemData[0])
    itemValue = int(itemData[1])
    items = [(itemWeight, itemValue, itemNumber)]

    # create rest of items variable
    for i in range(2, len(itemData) - 1, 2):
        itemNumber += 1
        itemWeight = int(itemData[i])
        itemValue = int(itemData[i + 1])
        items.append((itemWeight, itemValue, itemNumber))

    # run exhaustive method
    if method == "E":
        knapsack = exhaustiveMethod(sackWeight, numberOfItems, items)

    # run heuristic method
    elif method == "H":
        knapsack = heuristicMethod(sackWeight, items)

    # calculate total value
    value = 0
    for i in range(len(knapsack)):
        value += knapsack[i][1]

    # print value and item numbers
    print("\n%d" % value)
    for i in range(len(knapsack) - 1):
        print("%d " % knapsack[i][2], end='')
    print("%d" % knapsack[len(knapsack) - 1][2])

    endTime = time.time()
    runTime = endTime - startTime
    print("\nRuntime: {}".format(runTime))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
