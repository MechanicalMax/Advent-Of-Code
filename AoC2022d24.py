#Used hyper-neutrino to ensure proper execution of BFS
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
import math
from collections import deque

puz = getPuzzle.getPuzzleObject(__file__)

def parseGrid(lns):
    blizzards = tuple(set() for _ in range(4))

    for row, line in enumerate(lns[1:]):
        for col, ele in enumerate(line[1:]):
            if ele in "<>^v":
                blizzards["<>^v".find(ele)].add((row, col))

    return blizzards, row, col

def findFewestMinutes(lns):
    blizzards, endRow, endCol = parseGrid(lns)

    queue = deque([(0, -1, 0, 0)])
    seen = set()
    targets = [(endRow, endCol - 1), (-1, 0)]
    firstLegTime = 0
    capturedFirstTime = False

    lcm = math.lcm(endRow, endCol)
    
    while queue:
        time, curRow, curCol, stage = queue.popleft()

        time += 1

        for dRow, dCol in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
            nxtRow = curRow + dRow
            nxtCol = curCol + dCol

            nxtStage = stage

            if (nxtRow, nxtCol) == targets[stage % 2]:
                if stage == 2:
                    return firstLegTime, time
                if stage == 0 and not capturedFirstTime:
                    capturedFirstTime = True
                    firstLegTime = time
                nxtStage += 1                

            if(nxtRow < 0 or nxtCol < 0 or nxtRow >= endRow or nxtCol >= endCol) and (nxtRow, nxtCol) not in targets:
                continue

            fail = False

            if (nxtRow, nxtCol) not in targets:
                for i, testRow, testCol in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    if ((nxtRow - testRow * time) % endRow, (nxtCol - testCol * time) % endCol) in blizzards[i]:
                        fail = True
                        break
            
            if not fail:
                key = (nxtRow, nxtCol, nxtStage, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, nxtRow, nxtCol, nxtStage))

def partA(puz):
    ans = findFewestMinutes(lines)[0]
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findFewestMinutes(lines)[1]
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)