#Used hyper-neutrino
#Learned another application of complex numbers
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

moves = [-1j, 1j, -1, 1]
neighborOffsets = [-1 - 1j, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1]

#What tiles need to be checked for each direction
scanmap = {
    -1j: [-1j - 1, -1j, -1j + 1],
    1j: [1j - 1, 1j, 1j + 1],
    1: [1 - 1j, 1, 1 + 1j],
    -1: [-1 - 1j, -1, -1 + 1j]
}

def getElfPositions(lns):
    elves = set()
    for row, line in enumerate(lns):
        for col, ele in enumerate(line):
            if ele == "#":
                elves.add(col + row * 1j)
    return elves

def findEmptyTiles(positions):
    minX = min(x.real for x in positions)
    maxX = max(x.real for x in positions)
    minY = min(x.imag for x in positions)
    maxY = max(x.imag for x in positions)

    return int(((maxX - minX + 1) * (maxY - minY + 1)) - len(positions))

def simulateRounds(lns):
    elves = getElfPositions(lns)
    roundTenElves = None
    lastElves = set(elves)
    round = 1

    while(True):
        once = set()
        twice = set()

        for elf in elves:
            if all(elf + x not in elves for x in neighborOffsets):
                continue
            for move in moves:
                if all(elf + x not in elves for x in scanmap[move]):
                    prop = elf + move
                    if prop in twice:
                        pass
                    elif prop in once:
                        twice.add(prop)
                    else:
                        once.add(prop)
                    break

        elfClones = set(elves)

        for elf in elfClones:
            if all(elf + x not in elfClones for x in neighborOffsets):
                continue
            for move in moves:
                if all(elf + x not in elfClones for x in scanmap[move]):
                    prop = elf + move
                    if prop not in twice:
                        elves.remove(elf)
                        elves.add(prop)
                    break

        moves.append(moves.pop(0))

        if lastElves == elves:
            break
        elif round == 10:
            roundTenElves = set(elves)

        lastElves = set(elves)
        round += 1

    return findEmptyTiles(roundTenElves), round

def partA(puz):
    ans = simulateRounds(lines)[0]
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = simulateRounds(lines)[1]
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)