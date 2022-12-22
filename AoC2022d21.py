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

def findHumanValue(lns):
    monkeys = getMonkeys(lns)
    
    rootMonkeyOne, _, rootMonkeyTwo = monkeys["root"]
    monkeyOneValue, includesHuman = getMonkeyValue(rootMonkeyOne, monkeys)
    goalNum = 0
    if includesHuman:
        goalNum = getMonkeyValue(rootMonkeyTwo, monkeys)[0]
    else:
        goalNum = monkeyOneValue

    #Go backwards until hit human with goalNum

    return goalNum

def partA(puz):
    ans = getRootValue(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findHumanValue(lines)
    submit.safeSubmit(puz, ans, 'b')

#print(getMonkeys(puz.example_data.splitlines()))
#print(getRootValue(puz.example_data.splitlines()))
#print(54703080378102)
#partA(puz)
print(findHumanValue(puz.example_data.splitlines()))
#partB(puz)