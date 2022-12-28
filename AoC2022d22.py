#Solved part A relatively fast, but part B took days longer than
#it should have. So, I went back to hyper-neutrino to figure out
#where the errors were in my part b attempt. I ended up adapting his
#code to solve part B
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
import re

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

def simpleWrap(pos, offX, offY, openT, walls):
    nextPos = (pos[0] - offX, pos[1] - offY)
    while nextPos in openT or nextPos in walls:
        nextPos = (nextPos[0] - offX, nextPos[1] - offY)
    nextPos = (nextPos[0] + offX, nextPos[1] + offY)
    return nextPos

def findFinalPosition(inputData):
    openT, walls, directions = getMapInfo(inputData)
    pos = openT[0]
    directionIndex = 0

    for step in directions:
        if type(step) == int:
            for _ in range(step):
                offX, offY = facing[directionIndex]
                nextPos = (pos[0] + offX, pos[1] + offY)
                nextDirI = directionIndex

                if nextPos in openT:
                    pos = nextPos
                    continue

                if nextPos in walls:
                    break
                
                nextPos = simpleWrap(pos, offX, offY, openT, walls)

                if nextPos in walls:
                    break
                else:
                    pos = nextPos
                    directionIndex = nextDirI
        else:
            if step == 'R':
                directionIndex += 1
                directionIndex %= 4
            else:
                directionIndex -= 1
                if directionIndex < 0:
                    directionIndex += 4
    return pos[0], pos[1], directionIndex

#Used hyper-neutrino's solution as a guide for this function
def findFinalCubePosition(inputData):
    grid = []
    doneParsingGrid = False

    for line in inputData.splitlines():
        if line == "":
            doneParsingGrid = True
        if doneParsingGrid:
            sequence = line
        else:
            grid.append(line)

    #apply length to every element in grid and find max val
    width = max(map(len, grid))
    grid = [line + " " * (width - len(line)) for line in grid]

    r = 0
    c = 0
    dr = 0
    dc = 1

    #Find starting point
    while grid[r][c] != ".":
        c += 1

    for x, y in re.findall(r"(\d+)([RL]?)", sequence):
        x = int(x)
        for _ in range(x):
            cdr = dr
            cdc = dc
            nr = r + dr
            nc = c + dc
            #Go through every warp case
            if nr < 0 and 50 <= nc < 100 and dr == -1:
                dr, dc = 0, 1
                nr, nc = nc + 100, 0
            elif nc < 0 and 150 <= nr < 200 and dc == -1:
                dr, dc = 1, 0
                nr, nc = 0, nr - 100
            elif nr < 0 and 100 <= nc < 150 and dr == -1:
                nr, nc = 199, nc - 100
            elif nr >= 200 and 0 <= nc < 50 and dr == 1:
                nr, nc = 0, nc + 100
            elif nc >= 150 and 0 <= nr < 50 and dc == 1:
                dc = -1
                nr, nc = 149 - nr, 99
            elif nc == 100 and 100 <= nr < 150 and dc == 1:
                dc = -1
                nr, nc = 149 - nr, 149
            elif nr == 50 and 100 <= nc < 150 and dr == 1:
                dr, dc = 0, -1
                nr, nc = nc - 50, 99
            elif nc == 100 and 50 <= nr < 100 and dc == 1:
                dr, dc = -1, 0
                nr, nc = 49, nr + 50
            elif nr == 150 and 50 <= nc < 100 and dr == 1:
                dr, dc = 0, -1
                nr, nc = nc + 100, 49
            elif nc == 50 and 150 <= nr < 200 and dc == 1:
                dr, dc = -1, 0
                nr, nc = 149, nr - 100
            elif nr == 99 and 0 <= nc < 50 and dr == -1:
                dr, dc = 0, 1
                nr, nc = nc + 50, 50
            elif nc == 49 and 50 <= nr < 100 and dc == -1:
                dr, dc = 1, 0
                nr, nc = 100, nr - 50
            elif nc == 49 and 0 <= nr < 50 and dc == -1:
                dc = 1
                nr, nc = 149 - nr, 0
            elif nc < 0 and 100 <= nr < 150 and dc == -1:
                dc = 1
                nr, nc = 149 - nr, 50
            if grid[nr][nc] == "#":
                dr = cdr
                dc = cdc
                break
            r = nr
            c = nc
        if y == "R":
            dr, dc = dc, -dr
        elif y == "L":
            dr, dc = -dc, dr

    #Find direction offset
    if dr == 0:
        if dc == 1:
            facing = 0
        else:
            facing = 2
    else:
        if dc == 1:
            facing = 1
        else:
            facing = 3

    return r+1, c+1, facing

def finalPassword(inputData, cubewrap=False):
    if cubewrap:
        row, col, facing = findFinalCubePosition(inputData)
    else:
        row, col, facing = findFinalPosition(inputData)
    return row*1000 + col*4 + facing

def partA(puz):
    ans = finalPassword(puz.input_data)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = finalPassword(puz.input_data, cubewrap=True)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)