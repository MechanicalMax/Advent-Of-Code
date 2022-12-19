#Used tutorial on YouTube; Thank you hyper-neutrino
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
from collections import deque

puz = getPuzzle.getPuzzleObject(__file__)

# Get valve pressure and connections for each node
def getValves(lns):
    valves = {}
    tunnles = {}
    for line in lns:
        line = line.strip()
        valve = line.split()[1]
        flow = int(line.split(";")[0].split("=")[1])
        connections = line.split("to ")[1].split(" ", 1)[1].split(", ")
        valves[valve] = flow
        tunnles[valve] = connections
    return valves, tunnles

# Get the distances to each valve that releases pressure
def getCollapsedDistances(valves, tunnles):
    dists = {}
    nonempty = []

    for valve in valves:
        if valve != "AA" and not valves[valve]: #if not start and valve releases pressure
            continue #skip

        if valve != "AA":
            nonempty.append(valve)

        dists[valve] = {valve: 0, "AA": 0}
        visited = {valve}

        queue = deque([(0, valve)])

        while queue:
            distance, position = queue.popleft()
            for neighbor in tunnles[position]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if valves[neighbor]:
                    dists[valve][neighbor] = distance + 1
                queue.append((distance + 1, neighbor))

        del dists[valve][valve]
        if valve != "AA":
            del dists[valve]["AA"]

    return dists, nonempty

#Depth First Search with heavy optimizations
#Bitmask used to keep track of already visited positions in cache
def dfs(time, valve, bitmask, dists, valves, indicies, cache):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indicies[neighbor]
        if bitmask & bit:
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit, dists, valves, indicies, cache) + valves[neighbor] * remtime)
    cache[(time, valve, bitmask)] = maxval
    return maxval

def getMaxPressure(lns, partner = False):
    valves, tunnles = getValves(lns)
    dists, nonempty = getCollapsedDistances(valves, tunnles)

    indicies = {}
    for index, element in enumerate(nonempty):
        indicies[element] = index

    cache = {}

    maxPressure = 0

    if partner:
        #Assume the partner already closed their valves
        b = (1 << len(nonempty)) - 1
        for i in range((b + 1) // 2):
            maxPressure = max(maxPressure, dfs(26, "AA", i, dists, valves, indicies, cache) + dfs(26, "AA", b ^ i, dists, valves, indicies, cache))
    else:
        maxPressure = dfs(30, "AA", 0, dists, valves, indicies, cache)

    return maxPressure

def partA(puz):
    ans = getMaxPressure(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = getMaxPressure(lines, partner=True)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)