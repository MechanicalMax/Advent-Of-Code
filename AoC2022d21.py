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

def getMonkeyValue(name, monkeys):
    if type(monkeys[name]) == int:
        return monkeys[name]
    else:
        firstName, opp, secondName = monkeys[name]
        firstMonkey = getMonkeyValue(firstName, monkeys)
        secondMonkey = getMonkeyValue(secondName, monkeys)
        value = 0
        if opp == '+':
            value = firstMonkey + secondMonkey
        elif opp == '-':
            value = firstMonkey - secondMonkey
        elif opp == '*':
            value = firstMonkey * secondMonkey
        else:
            value = firstMonkey / secondMonkey
        return value

def getRootValue(lns):
    monkeys = getMonkeys(lns)
    
    return int(getMonkeyValue("root", monkeys))

def partA(puz):
    ans = getRootValue(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'b')

print(getMonkeys(puz.example_data.splitlines()))
print(getRootValue(puz.example_data.splitlines()))
partA(puz)
#partB(puz)