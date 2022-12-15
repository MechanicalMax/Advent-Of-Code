import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
import math

puz = getPuzzle.getPuzzleObject(__file__)

class Monkey:
    def __init__(self, part, items, operation, operationConstant, divisibilty, trueMonkey, falseMonkey):
        self.part = part
        self.items = items
        self.operation = operation
        self.operationConstant = operationConstant
        self.divisibility = int(divisibilty)
        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)
        self.inspections = 0

    def inspectItems(self, lcm):
        newItemLocations = []
        newItems = []
        for item in self.items:
            item = self.applyOperation(item)
            self.inspections += 1
            
            if self.part == 'a':
                item //= 3
            elif self.part == 'b':
                item %= lcm
            else:
                print(f"{self.part} is invalid")

            if self._checkDivisibility(item):
                newItemLocations.append(self.trueMonkey)
            else:
                newItemLocations.append(self.falseMonkey)
            newItems.append(item)
        self.items = newItems
        return newItemLocations

    def applyOperation(self, item):
        return self._multiply(item) if self.operation == '*' else self._add(item)

    def _checkDivisibility(self, number):
        return True if number % self.divisibility == 0 else False

    def _getMultiple(self, number):
        multiple = self.operationConstant
        if multiple == 'old':
            multiple = number
        else:
            multiple = int(multiple)
        return multiple

    def _multiply(self, number):
        multiple = self._getMultiple(number)
        return number * multiple

    def _add(self, number):
        multiple = self._getMultiple(number)
        return number + multiple

def createMonkeys(lns, part):
    monkeyArray = []

    for lnum in range(len(lns)):
        multiple = (lnum+7) % 7
        if multiple == 0:
            currentMonkeyInfo = [part]
        elif multiple == 1:
            currentMonkeyInfo.append(getStartingItemsArray(lns[lnum]))
        elif multiple == 2:
            currentMonkeyInfo.append(lns[lnum][23]) #operation
            currentMonkeyInfo.append(lns[lnum][25:]) #number or "old"
        elif multiple == 3:
            currentMonkeyInfo.append(lns[lnum][21:])
        elif multiple == 4:
            currentMonkeyInfo.append(lns[lnum][29:])
        elif multiple == 5:
            currentMonkeyInfo.append(lns[lnum][30:])
        else:
            monkeyArray.append(Monkey(*currentMonkeyInfo))
    monkeyArray.append(Monkey(*currentMonkeyInfo))

    return monkeyArray

def simulateNextRound(monkeyArray, lcm):
    for i in range(len(monkeyArray)):
        monkey = monkeyArray[i]
        pointers = monkey.inspectItems(lcm)
        for pointer in pointers:
            monkeyArray[pointer].items.append(monkey.items.pop(0))
    return monkeyArray

def getStartingItemsArray(line):
    return list(map(int, line[18:].split(", ")))

def calculateMonkeyBusiness(mArr):
    maxCounts = [0, 0]
    for monkey in mArr:
        for i in range(len(maxCounts)):
            if monkey.inspections > maxCounts[i]:
                maxCounts.insert(i, monkey.inspections)
                maxCounts.pop()
                break
    return maxCounts[0] * maxCounts[1]

def getLCM(monkeyArray):
    divisibilities = []
    for monkey in monkeyArray:
        divisibilities.append(monkey.divisibility)
    return math.lcm(*divisibilities)

def simulateRounds(lns, part):
    monkeyArray = createMonkeys(lns, part)
    rounds = 20 if part == 'a' else 10000
    lcm = 0 if part == 'a' else getLCM(monkeyArray)

    for round in range(rounds):
        monkeyArray = simulateNextRound(monkeyArray, lcm)

    return calculateMonkeyBusiness(monkeyArray)    

def partA(puz):
    ans = simulateRounds(lines, 'a')
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = simulateRounds(lines, 'b')
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)