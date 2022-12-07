import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getNewPath(cmd, currentPath):
    newDir = cmd.split()[2]
    
    if (newDir == '..'):
        removedChar = ''
        while(removedChar != '/'):
            currentPath, removedChar = currentPath[:-1], currentPath[-1]
    else:
        currentPath = currentPath + '/' + cmd.split()[2]

    return currentPath

def sumSize(paths, path):
    pathSize = 0

    for item in paths[path]['pointers']:
        pathSize += sumSize(paths, item)

    for item in paths[path]['files']:
        pathSize += item['fileSize']

    return pathSize

def getPathTotals(cmds):
    paths = {}
    currentPath = ""

    for cmd in cmds:
        if cmd.startswith('$'):
            if 'cd' in cmd:
                currentPath = getNewPath(cmd, currentPath)
                if currentPath not in paths:
                    paths[currentPath] = {'size': 0, 'pointers': [], 'files': []}
        else:
            if cmd.startswith('dir'):
                paths[currentPath]['pointers'].append(currentPath + '/' + cmd[4:])
            else:
                fileSize, name = cmd.split()
                paths[currentPath]['files'].append({'fileSize': int(fileSize), 'name':name})

    for path in paths:
        paths[path]['size'] = sumSize(paths, path)

    return paths

def sumDir(commands, atMost):
    paths = getPathTotals(commands)
    total = 0

    for path in paths:
        pathSize = paths[path]['size']
        if pathSize <= atMost:
            total += pathSize

    return total

def findMinDirForDel(commands, totalSpace):
    paths = getPathTotals(commands)
    freeSpace = totalSpace - paths['//']['size']
    requiredSpace = 30000000 - freeSpace
    minimumPossibleDir = 70000000

    for path in paths:
        pathSize = paths[path]['size']
        if pathSize >= requiredSpace and pathSize < minimumPossibleDir:
            minimumPossibleDir = pathSize

    return minimumPossibleDir

def partA(puz):
    ans = sumDir(lines, 100000)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findMinDirForDel(lines, 70000000)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)