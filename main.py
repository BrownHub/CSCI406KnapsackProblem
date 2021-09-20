# KnapsackProblem
# author: Kendall Brown

from copy import copy

def exhaustiveMethod(sackWeight, numberOfItems, items):

    # initialize values and run recursive method
    tempSet = list()
    powerSet = list()
    powerSet = generatePowerSet(items, tempSet, numberOfItems, powerSet)

    # examine power set for ideal value
    ideal = 0
    for i in range(len(powerSet)):
        loadWeight = 0
        loadValue = 0
        # calculate wieght and value of each set
        for j in range(len(powerSet[i])):
            loadWeight += powerSet[i][j][0]
            loadValue += powerSet[i][j][1]

        # check that set is not overweight and compare for greatest value
        if loadWeight <= sackWeight:
            ideal = max(ideal, loadValue)

    return ideal

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
    value = 0

    # add items until sack is full
    for i in range(len(items)):
        if remainingWeight - items[i][0] > 0:
            remainingWeight -= items[i][0]
            value += items[i][1]

    return value

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

if __name__ == '__main__':

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

    # read data from file
    with open(filename) as inputFile:
        sackWeight = int(inputFile.readline())
        numberOfItems = int(inputFile.readline())
        itemsFromFile = inputFile.read()

    # create items variable using data for the first item
    itemData = itemsFromFile.split()
    itemWeight = int(itemData[0])
    itemValue = int(itemData[1])
    items = [(itemWeight, itemValue)]

    # create rest of items variable
    for i in range(2, len(itemData) - 1, 2):
        itemWeight = int(itemData[i])
        itemValue = int(itemData[i + 1])
        items.append((itemWeight, itemValue))

    # run exhaustive method
    if method == "E":
        print("\nThe greatest possible value is: ", end="")
        print(exhaustiveMethod(sackWeight, numberOfItems, items))
    # run heuristic method
    elif method == "H":
        print("\nThe best value is roughly: ", end="")
        print(heuristicMethod(sackWeight, items))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
