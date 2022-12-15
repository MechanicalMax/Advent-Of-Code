import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
from time import sleep

puz = getPuzzle.getPuzzleObject(__file__)

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def getMaze(lns):
    maze = []
    for line in lns:
        newRow = []
        for char in line:
            newRow.append(char)
        maze.append(newRow)
    return maze

def getEndpoints(maze):
    start = None
    end = None
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            ele = maze[row][col]
            if ele == 'S':
                start = Node(position=[row, col])
            elif ele == 'E':
                end = Node(position=[row, col])
            elif start and end:
                break
    return start, end

def fewestSteps(lns):
    maze = getMaze(lns)
    start, end = getEndpoints(maze)
    path = findPath(maze, start, end)
    print(path)
    return len(path)

def findPath(maze, start, end): #A* pathfinding
    openList = []
    closedList = []

    openList.append(start)

    while len(openList) > 0:
        sleep(.2)
        #find current node
        currentIndex = 0
        currentNode = openList[currentIndex]
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        #switch current node to closed list
        openList.pop(currentIndex)
        closedList.append(currentNode)

        print(currentNode.position)
        print("Open:")
        for item in openList:
            print(item.position, end=", ")
        print("\nClosed:")
        for item in closedList:
            print(item.position, end=", ")
        print()
        print()

        #Goal found
        if currentNode == end:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        #generate next possible children nodes
        children = []
        for newPosition in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nodePosition = [currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1]]

            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[0]) - 1) or nodePosition[1] < 0:
                continue

            # if height is greater than one plus current node
            currentLetter = maze[currentNode.position[0]][currentNode.position[1]]
            newLetter = maze[nodePosition[0]][nodePosition[1]] 
            if currentLetter != 'S':
                if newLetter == 'S':
                    continue
                if (ord(newLetter) > 1 + ord(currentLetter)):
                    continue

            newNode = Node(parent=currentNode, position=nodePosition)

            children.append(newNode)

        for child in children:
            for closedChild in closedList:
                if child == closedChild:
                    continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2)
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue
            openList.append(child)

def partA(puz):
    ans = fewestSteps(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'b')

print(fewestSteps(puz.example_data.splitlines()))