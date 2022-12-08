#Part A - Imagine Refactoring
#Part B - Make sure to read the problem correctly
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def toGrid(lns, type):
    grid = []
    for line in lns:
        lineArr = []
        for ele in line:
            if type == 'Visible':
                lineArr.append({'height': int(ele), 'visible': False})
            else:
                lineArr.append(int(ele))
        grid.append(lineArr)
    return grid

def getTreeLine(grid, row, col, score):
    treeArr = []
    sideLen = len(grid)

    if score == 'up':
        for currentRow in range(row - 1, -1, -1):
            treeArr.append(grid[currentRow][col])
    elif score == 'left':
        treeArr = grid[row][:col]
        treeArr = treeArr[::-1]
    elif score == 'right':
        treeArr = grid[row][col+1:]
    elif score == 'down':
        for currentRow in range(row + 1, sideLen):
            treeArr.append(grid[currentRow][col])
    else:
        print(f"{score} not possible")

    return treeArr

def getScenicScore(grid, row, col):
    scores = {'up': 0, 'left': 0, 'right': 0, 'down': 0}
    startHeight = grid[row][col]

    for score in scores.keys():
        treesInLine = getTreeLine(grid, row, col, score)
        for i in range(len(treesInLine)):
            scores[score] += 1
            if treesInLine[i] >= startHeight:
                break

    scenicScore = 1
    for score in scores.values():
        scenicScore *= score

    return scenicScore

def findHighestScenicScore(lns):
    grid = toGrid(lns, 'basic')

    maxScore = 0

    for row in range(1, len(lns)-1):
        for col in range(1, len(lns)-1):
            currentScore = getScenicScore(grid, row, col)
            if currentScore > maxScore:
                maxScore = currentScore

    return maxScore

def countVisibleTrees(lns):
    insideTrees = len(lns) - 1
    grid = toGrid(lns, 'Visible')
    visible = insideTrees * 4

    #left
    for row in range(1, insideTrees):
        currentTallest = grid[row][0]['height']
        for tree in range(0, insideTrees):
            currentHeight = grid[row][tree]['height']
            if(currentHeight > currentTallest):
                currentTallest = currentHeight
                if grid[row][tree]['visible'] == False:
                    visible += 1
                    grid[row][tree]['visible'] = True

    #right
    for row in range(1, insideTrees):
        currentTallest = grid[row][insideTrees]['height']
        for tree in range(insideTrees - 1, 0, -1):
            currentHeight = grid[row][tree]['height']
            if(currentHeight > currentTallest):
                currentTallest = currentHeight
                if grid[row][tree]['visible'] == False:
                    visible += 1
                    grid[row][tree]['visible'] = True

    #top
    for col in range(1, insideTrees):
        currentTallest = grid[0][col]['height']
        for tree in range(0, insideTrees):
            currentHeight = grid[tree][col]['height']
            if(currentHeight > currentTallest):
                currentTallest = currentHeight
                if grid[tree][col]['visible'] == False:
                    visible += 1
                    grid[tree][col]['visible'] = True

    #bottom
    for col in range(1, insideTrees):
        currentTallest = grid[insideTrees][col]['height']
        for tree in range(insideTrees - 1, 0, -1):
            currentHeight = grid[tree][col]['height']
            if(currentHeight > currentTallest):
                currentTallest = currentHeight
                if grid[tree][col]['visible'] == False:
                    visible += 1
                    grid[tree][col]['visible'] = True

    return visible

def partA(puz):
    ans = countVisibleTrees(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findHighestScenicScore(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)