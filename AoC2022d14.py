#Very inefficient part B; however, it still works
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getNumber(line, index):
    num = 0
    while index < len(line) and line[index].isnumeric():
        num *= 10
        num += int(line[index])
        index += 1
    return num, index

def getPointFromIndex(ln, i):
    x, i = getNumber(ln, i)
    i += 1
    y, i = getNumber(ln, i)
    return x, y, i + 4

def getEndpoints(line):
    endpoints = []
    i = 0
    while i <= len(line):
        newX, newY, newI = getPointFromIndex(line, i)
        endpoints.append((newX, newY))
        i = newI
    return endpoints

def findSolidPoints(lns):
    solidPoints = []
    for line in lns:
        endpoints = getEndpoints(line)
        for i in range(len(endpoints)-1):
            start = endpoints[i]
            end = endpoints[i+1]
            if start[0] == end[0]:
                for newY in range(start[1],end[1], 1-2*(start[1]>end[1])):
                    solidPoints.append((end[0], newY))
            else:
                for newX in range(start[0],end[0], 1-2*(start[0]>end[0])):
                    solidPoints.append((newX, end[1]))
        solidPoints.append(endpoints[-1])
    solidPoints.sort()
    return solidPoints

def findMaxDepth(solidPoints):
    return max(solidPoints, key=lambda tup: tup[1])[1] + 1

def applyOffset(point, direction=None):
    xOff = 0
    if direction == 'Left':
        xOff = -1
    elif direction == 'Right':
        xOff = 1
    return(point[0]+xOff, point[1]+1)

def isNotSolid(point, solid, maxDepth):
    solidPoint = False
    if point[1] >= maxDepth + 1 or point in solid:
        solidPoint = True
    return not solidPoint

def dropSand(solid, maxDepth):
    position = (500, 0)
    falling = True
    notEndless = True

    while(falling and notEndless):
        if isNotSolid(applyOffset(position), solid, maxDepth):
            position = applyOffset(position)
            if position[1] >= maxDepth:
                solid.append(position)
                notEndless = False
        elif isNotSolid(applyOffset(position, 'Left'), solid, maxDepth):
            position = applyOffset(position, 'Left')
        elif isNotSolid(applyOffset(position, 'Right'), solid, maxDepth):
            position = applyOffset(position, 'Right')
        else:
            solid.append(position)
            temp = applyOffset(applyOffset(position))
            if temp in solid:
                del solid[solid.index(temp)]
            falling = False

    return notEndless, solid, position

def findRestingSandUnits(lns):
    solidPoints = findSolidPoints(lns)
    maxDepth = findMaxDepth(solidPoints)
    restingSand = -1
    notFlowing = True

    while(notFlowing):
        notFlowing, solidPoints, _ = dropSand(solidPoints, maxDepth)
        restingSand += 1
        print(_)

    return restingSand

def findTotalSandUnits(lns):
    solidPoints = findSolidPoints(lns)
    maxDepth = findMaxDepth(solidPoints)
    restingSand = 0
    pouring = True

    while(pouring):
        _, solidPoints, restPosition = dropSand(solidPoints, maxDepth)
        if restPosition == (500, 0):
            pouring = False
        restingSand += 1
        print(restPosition)

    return restingSand

def partA(puz):
    ans = findRestingSandUnits(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findTotalSandUnits(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)