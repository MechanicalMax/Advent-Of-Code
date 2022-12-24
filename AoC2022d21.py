#Finally an easier one! Part a was straightforward with recursion
#My solution to part b could be refactored, but it still works
#fast
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getMonkeys(lns):
    monkeys = {}
    for line in lns:
        name = line[:4]
        monkeys[name] = line[6:]
        if monkeys[name][0].isnumeric():
            monkeys[name] = int(monkeys[name])
        else:
            monkeyOpp = (monkeys[name][:4], monkeys[name][5], monkeys[name][7:])
            monkeys[name] = monkeyOpp
    return monkeys

def getMonkeyValue(name, monkeys, includesHuman = False):
    if type(monkeys[name]) == int:
        if name == 'humn':
            includesHuman = True
        return monkeys[name], includesHuman
    else:
        firstName, opp, secondName = monkeys[name]
        firstMonkey, includesHuman = getMonkeyValue(firstName, monkeys, includesHuman)
        secondMonkey, includesHuman = getMonkeyValue(secondName, monkeys, includesHuman)
        value = 0
        if opp == '+':
            value = firstMonkey + secondMonkey
        elif opp == '-':
            value = firstMonkey - secondMonkey
        elif opp == '*':
            value = firstMonkey * secondMonkey
        else:
            value = firstMonkey / secondMonkey
        return value, includesHuman

def getRootValue(lns):
    monkeys = getMonkeys(lns)
    return int(getMonkeyValue("root", monkeys)[0])

def getInverseValue(name, equalTo, monkeys):
    leftMonkey, opp, rightMonkey = monkeys[name]
    solveForLeft = False
    value = 0

    leftMonkeyValue, includesHuman = getMonkeyValue(leftMonkey, monkeys)
    if includesHuman:
        rightMonkeyValue = getMonkeyValue(rightMonkey, monkeys)[0]
        solveForLeft = True

    if solveForLeft:
        if opp == '+':
            value = equalTo - rightMonkeyValue
        elif opp == '-':
            value = equalTo + rightMonkeyValue
        elif opp == '*':
            value = equalTo / rightMonkeyValue
        else:
            value = equalTo * rightMonkeyValue
    else:
        if opp == '+':
            value = equalTo - leftMonkeyValue
        elif opp == '-':
            value = leftMonkeyValue - equalTo
        elif opp == '*':
            value = equalTo / leftMonkeyValue
        else:
            value = leftMonkeyValue / equalTo
    
    if rightMonkey != 'humn' and leftMonkey != 'humn':    
        value = getInverseValue(leftMonkey if solveForLeft else rightMonkey, value, monkeys)
    return value

def findHumanValue(lns):
    monkeys = getMonkeys(lns)
    rootMonkeyOne, _, rootMonkeyTwo = monkeys["root"]
    monkeyOneValue, includesHuman = getMonkeyValue(rootMonkeyOne, monkeys)
    goalNum = 0
    humnVal = 0
    if includesHuman:
        goalNum = getMonkeyValue(rootMonkeyTwo, monkeys)[0]
        humnVal = getInverseValue(rootMonkeyOne, goalNum, monkeys)
    else:
        goalNum = monkeyOneValue
        humnVal = getInverseValue(rootMonkeyTwo, goalNum, monkeys)

    return int(humnVal)

def partA(puz):
    ans = getRootValue(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findHumanValue(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)