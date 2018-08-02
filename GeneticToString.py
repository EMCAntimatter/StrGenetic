import os
import signal
import unicodedata
import random
import time
import threading


def strToNumList(i):
    out = list((ord(i[x - 1]) for x in range(i.__len__())))
    return out


def genMutatedList(iList):
    for i in range(iList.__len__()):
        x = int(random.normalvariate(iList[i], random.randint(0, 10)))
        if x > 127:
            x = 127
        elif x < 32:
            x = 32
        iList[i] = x

    return iList


def listOfMutatedLists(input, lists):
    output = list(())
    for i in range(lists):
        output.append(genMutatedList(input))
        if output[i].__len__() == 0:
            output[output.__len__() - 1] = [0 for i in goalNumList]
    for i in output:
        del i[goalString.__len__():]
        for x in range(i.__len__() - 1):
            i[x] = random.randint(32, 127)

    return output


def fitness(input):
    output = 0
    for i in range(input.__len__()):
        output += abs(goalNumList[i]-input[i])
    return output

def randList():
    output = list(())
    for x in range(goalString.__len__() + 1):
        output.append(int(random.normalvariate(128 / 2, 5)))
    for i in output:
        if i < 32:
            i = 32
        elif i > 127:
            i = 127
        if type(i) == 'float':
            i = int(i)
    return output


def findHighestInNestedArrayAtIndex(fitness, index):
    highestIndexObject = fitness[0]
    for i in fitness:
        if i.__len__() <= index:
            print("Index Overflow")
        elif abs(goalNumList[index] - i[index]) > abs(goalNumList[index] - highestIndexObject[index]):
            highestIndexObject = i
    return highestIndexObject[index]


def bestGenes(fitness, storage):
    output = list(())
    for i in range(goalString.__len__()):
        output.append(findHighestInNestedArrayAtIndex(storage, i))
        ++i
    return output


def newGeneration(input, listsPerGen):
    storage = listOfMutatedLists(input, listsPerGen)
    fitnessStorage = list((fitness(i) for i in storage))
    return bestGenes(fitnessStorage, storage)


def numListToString(iList):
    output = ""
    for i in range(iList.__len__()):
        output = output + str(chr(iList[i]))
    return output


def remove_control_characters(s):
    out = ""
    for ch in s:
        if unicodedata.category(ch)[0] != "C":
            out.join(ch)
        else:
            out.join(" ")
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

def randCharIntVal():
    return random.randint(32, 127)

goalString = "String"
print(goalString)
print(goalString.__len__())
time.sleep(1)
# goalString = input("Enter the goal string (Unicode block 1 and no control characters):\n")
goalNumList = strToNumList(goalString)
maxGens = 10000
# maxGens = input("Max Number of Generations")
listsPerGen = 1
# listsPerGen = input("Lists Per Generation: \n")

currentList = randList()
bestSoFar = currentList
gen = 0

while gen <= maxGens and currentList != goalNumList:
    currentList = ()
    currentList = newGeneration(bestSoFar, listsPerGen)
    # currentList = list(strToNumList(remove_control_characters(numListToString(currentList))))
    print("String:", numListToString(currentList), "| Chars", currentList.__len__(), "| Fitness:", fitness(currentList), "| Gen:", gen, end="")
    #print(currentList, end="")
    # print(currentList)
    if fitness(currentList) <= fitness(bestSoFar):
        bestSoFar = currentList
        print("Best!!", end="")
    print("")
    gen = gen + 1

print(numListToString(bestSoFar), "|", bestSoFar, "|", fitness(bestSoFar))
