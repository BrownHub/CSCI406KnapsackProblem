
import random

def generateExhaustive():
    knapsackWeight = int(200 * random.random() + 100)
    numItems = int(10 * random.random() + 15)

    with open("ExhaustiveData.txt", "w") as exhaustiveFile:
        exhaustiveFile.write("{}\n".format(knapsackWeight))
        exhaustiveFile.write("{}\n".format(numItems))

        for i in range(numItems):
            weight = int(80 * random.random())
            value = int(320 * random.random() + 30)
            exhaustiveFile.write("{} {}\n".format(weight, value))

def generateHeuristic():
    knapsackWeight = int(200 * random.random() + 100)
    numItems = int(60 * random.random() + 70)

    with open("HeuristicData.txt", "w") as heuristicFile:
        heuristicFile.write("{}\n".format(knapsackWeight))
        heuristicFile.write("{}\n".format(numItems))

        for i in range(numItems):
            weight = int(80 * random.random())
            value = int(320 * random.random() + 30)
            heuristicFile.write("{} {}\n".format(weight, value))