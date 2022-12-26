import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

facing = [(0,1), (1,0), (0,-1), (-1,0)]

def parseDirections(directions):
    formattedDirections = []
    tempNum = 0
    for char in directions:
        if char.isnumeric():
            tempNum *= 10
            tempNum += int(char)
        else:
            formattedDirections.append(tempNum)
            tempNum = 0
            formattedDirections.append(char)
    formattedDirections.append(tempNum)
    return formattedDirections

def getMapInfo(inputData):
    maze, directions = inputData.split("\n\n")
    maze = maze.splitlines()
    openTiles, walls = [], []
    
    for rowIndex, row in enumerate(maze):
        for col in range(len(row)):
            if row[col] == '.':
                openTiles.append((rowIndex+1,col+1))
            elif row[col] == '#':
                walls.append((rowIndex+1,col+1))

    directions = parseDirections(directions)
        
    return openTiles, walls, directions

def findFinalPosition(inputData):
    openT, walls, directions = getMapInfo(inputData)
    pos = openT[0]
    directionIndex = 0

    for step in directions:
        if type(step) == int:
            for unit in range(step):
                offX, offY = facing[directionIndex]
                nextPos = (pos[0] + offX, pos[1] + offY)

                if nextPos in openT:
                    pos = nextPos
                    continue

                if nextPos in walls:
                    break

                nextPos = (pos[0] - offX, pos[1] - offY)
                while nextPos in openT or nextPos in walls:
                    nextPos = (nextPos[0] - offX, nextPos[1] - offY)
                nextPos = (nextPos[0] + offX, nextPos[1] + offY)

                if nextPos in walls:
                    break
                else:
                    pos = nextPos
        else:
            if step == 'R':
                directionIndex += 1
                directionIndex %= 4
            else:
                directionIndex -= 1
                if directionIndex < 0:
                    directionIndex += 4

    return pos[0], pos[1], directionIndex

def finalPassword(inputData):
    row, col, facing = findFinalPosition(inputData)
    return row*1000 + col*4 + facing

def partA(puz):
    ans = finalPassword(puz.input_data)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
#partB(puz)