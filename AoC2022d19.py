#too difficult to do without resources,
#so I am using hyper-neutrino's YouTube walkthrough
#to get exposure to different search algorithms
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
import re

puz = getPuzzle.getPuzzleObject(__file__)

def getBlueprints(lns):
    blueprints = []
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
        blueprints.append([blueprint, maxspend])
    return blueprints

#Depth First Search
def dfs(blueprint, maxspend, cache, time, bots, resources):
    pass

def partA(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'b')

print(getBlueprints(lines))
#partA(puz)
#partB(puz)