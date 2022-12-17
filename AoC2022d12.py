import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
from heapq import heappop, heappush

puz = getPuzzle.getPuzzleObject(__file__)

def getMaze(lns):
    maze = []
    for line in lns:
        newRow = []
        for char in line:
            newRow.append(char)
        maze.append(newRow)
    return maze

def getStart(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'E':
                return row, col

def height(location):
    if location == 'S':
        return 0
    elif location == 'E':
        return 25
    elif location.islower:
        return ord(location) - 97

def possibleMoves(maze, row, col, steps):
    newPositions = []
    for rowOff, colOff in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        newRow = row + rowOff
        newCol = col + colOff

        if not (0 <= newRow < len(maze) and 0 <= newCol < len(maze[0])):
            continue

        if height(maze[newRow][newCol]) >= height(maze[row][col]) - 1:
            newPositions.append((newRow, newCol))
    return newPositions

def fewestSteps(lns, endChar): #dijkstra's
    maze = getMaze(lns)
    start = getStart(maze)
    visited = [[False] * len(maze[0]) for _ in range(len(maze))] #create len(maze) False arrays of length len(maze[0])
    closed = [(0, start[0], start[1])]

    while(True):
        steps, curRow, curCol = heappop(closed)
        
        if visited[curRow][curCol]:
            continue
        visited[curRow][curCol] = True

        if maze[curRow][curCol] == endChar:
            return steps

        for newPos in possibleMoves(maze, row=curRow, col=curCol, steps=steps+1):
            heappush(closed, (steps + 1, newPos[0], newPos[1]))

def partA(puz):
    ans = fewestSteps(lines, 'S')
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = fewestSteps(lines, 'a')
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)