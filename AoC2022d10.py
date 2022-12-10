import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getInstructionData(instruction):
    if instruction[0] == 'n':
        add = 0
        cycles = 1
    elif instruction[0] == 'a':
        add = int(instruction[5:])
        cycles = 2
    return add, cycles

def sumArr(arr):
    total = 0
    for value in arr:
        total += value
    return total

def displayNextPixel(cycle, x, multiple):
    if (cycle-1) % multiple == 0:
        print()

    if cycle % multiple in range(x,x+3):
        print("#",end="")
    else:
        print(".",end="")

def sumSignalStrengths(lns, multiple):
    instructionIndex = 0
    cycle = 1
    startCycle = 1
    x = 1
    strengthCycleValues = []

    while instructionIndex < len(lns):
        add, cycles = getInstructionData(lns[instructionIndex])

        for i in range(cycles):
            if (cycle + 20) % multiple == 0:
                strengthCycleValues.append(cycle*x)

            displayNextPixel(cycle,x, multiple)

            cycle += 1
            if not (cycle < startCycle + cycles):
                x += add
                startCycle = cycle

        instructionIndex += 1

    return sumArr(strengthCycleValues)
    
def partA(puz):
    ans = sumSignalStrengths(lines, 40)
    print()
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    sumSignalStrengths(lines, 40)
    ans = input("\nEnter Capital Letters => ")
    submit.safeSubmit(puz, ans, 'b')

longExample = "addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop"

partA(puz)
partB(puz)
#sumSignalStrengths(longExample.splitlines(), 40)