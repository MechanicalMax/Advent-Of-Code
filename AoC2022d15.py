#Simple and fast part A, slow part B
#A better approach for part B would have been compairing
#boundary line offsets to find where they intersect
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

def getSensors(lns, row):
    sensors = []
    beaconsInRow = []
    for line in lns:
        x = int(line[line.index("x")+2:line.index(",")])
        y = int(line[line.index("y")+2:line.index(":")])
        beaconX = int(line[line.rindex("x")+2:line.rindex(",")])
        beaconY = int(line[line.rindex("y")+2:])
        
        if beaconY == row and (beaconX, beaconY) not in beaconsInRow:
            beaconsInRow.append((beaconX, beaconY))

        radius = abs(x-beaconX) + abs(y-beaconY)
        sensors.append((x,y,radius))

    return sensors, len(beaconsInRow)

def getRange(sensor, row):
    start = sensor[0] - (sensor[2] - abs(row - sensor[1]))
    end = sensor[0] + (sensor[2] - abs(row - sensor[1]))
    return start, end

def getRanges(sensors, row):
    coveredRanges = []
    for s in sensors:
        start, end = getRange(s, row)
        if start <= end:
            coveredRanges.append((start, end))
    coveredRanges.sort()
    return coveredRanges

def unionRanges(ranges):
    coveredIntervals = [ranges[0]]
    for interval in ranges[1:]:
        if interval[0] <= coveredIntervals[-1][1]:
            if interval[1] > coveredIntervals[-1][1]:
                temp = coveredIntervals.pop()
                coveredIntervals.append((temp[0],interval[1]))
        else:
            coveredIntervals.append(interval)
    return coveredIntervals

def sumOpenPositions(lns, row):
    sensors, beaconsInRow = getSensors(lns, row)
    ranges = getRanges(sensors, row)
    uncheckedPositions = -beaconsInRow

    coveredIntervals = unionRanges(ranges)

    for interval in coveredIntervals:
        uncheckedPositions += 1 + interval[1] - interval[0]

    return uncheckedPositions

def findTuningFrequency(lns, max, min):
    signalX = -1
    signalY = -1
    for row in range(min, max+1):
        print(row)
        sensors, beaconsInRow = getSensors(lns, row)
        ranges = getRanges(sensors, row)
        coveredIntervals = unionRanges(ranges)

        if len(coveredIntervals) != 1:
            for i in range(len(coveredIntervals)-1):
                if coveredIntervals[i][1] + 2 == coveredIntervals[i+1][0] and min <= coveredIntervals[i][1] + 1 <= max:
                    signalY = row
                    signalX = coveredIntervals[i][1] + 1
                    return signalX * 4000000 + signalY

def partA(puz):
    ans = sumOpenPositions(lines, 2000000)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = findTuningFrequency(lines, 4000000, 0)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)