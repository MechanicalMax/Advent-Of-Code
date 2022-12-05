import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getNumberOfStacks(numberLine):
    stckNum = int(numberLine[len(numberLine)-2])
    return stckNum

def getStackData(lns):
    stackData = {}
    lineIndex = 0
    
    while('[' in lns[lineIndex]):
        lineIndex += 1
    
    numberOfStacks = getNumberOfStacks(lns[lineIndex])

    for i in range(numberOfStacks):
        stackData[i + 1] = []

    for strIndex in range(lineIndex-1, -1, -1):
        currentLine = lns[strIndex]
        for stack in range(numberOfStacks):
            crateSpace = currentLine[stack * 4: 3 + stack * 4]
            if crateSpace[1] != ' ':
                stackData[stack + 1].append(crateSpace[1])

    stackData['numStacks'] = numberOfStacks
    stackData['lineIndex'] = lineIndex

    return stackData

def getInstructionData(lns, firstInstructionIndex):
    data = []

    for line in lns[firstInstructionIndex + 2:]:
        lineParts = line.split(' ')
        data.append(
            {
                'num': int(lineParts[1]),
                'start': int(lineParts[3]),
                'end': int(lineParts[5])
            }
        )

    return data

def followInstructions(stacks, instructions,type):
    if(type == 9000):
        for instruction in instructions:
            for i in range(instruction['num']):
                stacks[instruction['end']].append(stacks[instruction['start']].pop())
    elif(type == 9001):
        for instruction in instructions:
            bottomCrateIndex = len(stacks[instruction['start']]) - instruction['num']
            stacks[instruction['end']] += stacks[instruction['start']][bottomCrateIndex:]
            stacks[instruction['start']] = stacks[instruction['start']][:bottomCrateIndex]
    else:
        print(f"Invalid type {type}")
    return stacks

def findTopCrates(lns, type):
    topCrates = ''
    stackData = getStackData(lns)
    instructionData = getInstructionData(lns, stackData['lineIndex'])
    stackData = followInstructions(stackData,instructionData,type)

    for i in range(int(stackData['numStacks'])):
        lastCrateIndex = len(stackData[i + 1]) - 1
        topCrates += stackData[i + 1][lastCrateIndex]
    
    return topCrates

def partA(puz):
    ans = findTopCrates(lines, 9000)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findTopCrates(lines, 9001)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)