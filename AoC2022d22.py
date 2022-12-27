import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

#right, down, left, up (increase is CW)
#<1,0>, <0,-1>, <-1,0>, <0,1>
#<0,1>, <-1,0>, <0,-1>, <1,0>
#<0,1>, <1,0>, <0,-1>, <-1,0>
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

#Hard coded for my puzzle input
def cubeWrap(pos, dirI):
    #Checked: 4s, 2s, 3s, 5s, 1s, 6s, 7s
    #Check directions***
    #print()
    #print(pos, dirI)
    print(pos)
    curY, curX = pos
    if dirI == 0: #right
        if curY <= 50: #7
            #print(7.1)
            dirI = 2
            pos = (150 - curY, 100)
        elif curY <= 100: #1
            #print(1.1)
            dirI = 3
            pos = (50, curY - 50 + 100)
        elif curY <= 150: #7
            #print(7.2)
            dirI = 2
            pos = (150 - curY, 150)
        else: #2
            #print(2.1)
            dirI = 3
            pos = (150, curY - 150 + 50)
    elif dirI == 1: #down
        if curX <= 50:#6
            #print(6.1)
            pos = (1, curX + 100)
        elif curX <= 100:#2
            #print(2.2)
            dirI = 2
            pos = (curX - 50 + 150, 50)
        else:#1
            #print(1.2)
            dirI = 2
            pos = (curX - 100 + 50, 100)
    elif dirI == 2: #left
        if curY <= 50:#5
            #print(5.1)
            dirI = 0
            pos = (150 - curY, 1)
        elif curY <= 100:#3
            #print(3.1)
            dirI = 1
            pos = (101, curY - 50)
        elif curY <= 150:#5
            #print(5.2)
            dirI = 0
            pos = (150 - curY, 51)
        else:#4
            #print(4.1)
            dirI = 1
            pos = (1, curY - 150 + 50)
    else: #up
        if curX <= 50:#3
            #print(3.2)
            dirI = 0
            pos = (curX + 50, 51)
        elif curX <= 100:#4
            #print(4.2)
            dirI = 0
            pos = (curX - 50 + 150, 1)
        else:#6
            #print(6.2)
            pos = (200, curX - 100)

    #print(pos, dirI)
    print(pos)
    return pos, dirI

def findFinalPosition(inputData, cubewrap):
    openT, walls, directions = getMapInfo(inputData)
    pos = openT[0]
    directionIndex = 0

    for step in directions:
        #print(step, pos, directionIndex)
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
                
                if cubewrap:
                    nextPos, nextDirI = cubeWrap(pos, directionIndex)
                else:
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
    #print(pos, directionIndex)
    print("-------")
    print(walls)
    return pos[0], pos[1], directionIndex

def finalPassword(inputData, cubewrap=False):
    row, col, facing = findFinalPosition(inputData, cubewrap)
    return row*1000 + col*4 + facing

def partA(puz):
    ans = finalPassword(puz.input_data)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = finalPassword(puz.input_data, cubewrap=True)
    submit.safeSubmit(puz, ans, 'b')

#partA(puz)
partB(puz)