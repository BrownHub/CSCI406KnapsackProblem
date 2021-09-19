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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
