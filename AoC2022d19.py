#too difficult to do without resources,
#so I am using hyper-neutrino's YouTube walkthrough
#to get exposure to different search algorithms
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
import re
from math import ceil

puz = getPuzzle.getPuzzleObject(__file__)

#Depth First Search
def dfs(blueprint, maxspend, cache, time, bots, resources):
    if time == 0:
        return resources[3]

    key = tuple([time, *bots, *resources])
    if key in cache:
        return cache[key]

    maxval = resources[3] + bots[3] * time

    for botType, recipe in enumerate(blueprint):
        if botType != 3 and bots[botType] >= maxspend[botType]:
            continue

        wait = 0
        for resourceAmount, resourceType in recipe:
            if bots[resourceType] == 0:
                break
            wait = max(wait, ceil((resourceAmount - resources[resourceType]) / bots[resourceType]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            tempBots = bots[:]
            tempResources = [x + y * (wait + 1) for x, y in zip(resources, bots)]
            for resourceAmount, resourceType in recipe:
                tempResources[resourceType] -= resourceAmount
            tempBots[botType] += 1
            for i in range(3):
                tempResources[i] = min(tempResources[i], maxspend[i] * remtime)
            maxval = max(maxval, dfs(blueprint, maxspend, cache, remtime, tempBots, tempResources))

    cache[key] = maxval
    return maxval

def getQualityLevels(lns):
    total = 0

    for i, line in enumerate(lns):
        blueprint = []
        maxspend = [0, 0, 0] #Maximum possible resource spend per turn optimization
        for section in line.split(": ")[1].split(". "):
            recipe = []
            for x, y in re.findall(r"(\d+) (\w+)", section):
                x = int(x)
                y = ["ore", "clay", "obsidian"].index(y)
                recipe.append((x, y))
                maxspend[y] = max(maxspend[y], x)
            blueprint.append(recipe)
        geodes = dfs(blueprint, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        total += (i + 1) * geodes

    return total

def findMostGeodes(lns):
    total = 1

    for line in lns[:3]:
        blueprint = []
        maxspend = [0, 0, 0] #Maximum possible resource spend per turn optimization
        for section in line.split(": ")[1].split(". "):
            recipe = []
            for x, y in re.findall(r"(\d+) (\w+)", section):
                x = int(x)
                y = ["ore", "clay", "obsidian"].index(y)
                recipe.append((x, y))
                maxspend[y] = max(maxspend[y], x)
            blueprint.append(recipe)
        geodes = dfs(blueprint, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
        total *= geodes

    return total

def partA(puz):
    ans = getQualityLevels(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findMostGeodes(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)