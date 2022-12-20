#Used YouTube Tutorial - Thanks again hyper-neutrino
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines
from collections import deque

puz = getPuzzle.getPuzzleObject(__file__)

#Offsets from the cube's center to get the location of the cube's faces
faceOffsets = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]

#Get points from input
def extractPoints(lns):
    points = []
    for line in lns:
        points.append(tuple([int(cord) for cord in line.split(",")]))
    return tuple(points)

def getBlobInfo(lns):
    faces = {}
    points = extractPoints(lns)
    #Bounding Box
    mx = my = mz = float("inf")
    Mx = My = Mz = -float("inf")

    #count the number of times each face appears
    for p in points:
        #Find if point creates new bounding box
        mx = min(mx, p[0])
        my = min(my, p[1])
        mz = min(mz, p[2])
        Mx = max(Mx, p[0])
        My = max(My, p[1])
        Mz = max(Mz, p[2])

        for dx, dy, dz in faceOffsets:
            currentFace = (p[0] + dx, p[1] + dy, p[2] + dz)
            if currentFace not in faces:
                faces[currentFace] = 0
            faces[currentFace] += 1

    #Expand bounding box by 1
    mx -= 1
    my -= 1
    mz -= 1
    Mx += 1
    My += 1
    Mz += 1

    return faces, points, mx, my, mz, Mx, My, Mz

def getSurfaceArea(lns):
    faces, _, _, _, _, _, _, _ = getBlobInfo(lns)
    #count the number of faces that occur once (twice would mean the face is covered)
    return list(faces.values()).count(1)

#Find air spaces with a Breadth First Search
def findAirPoints(blobPoints, mx, my, mz, Mx, My, Mz):
    q = deque([(mx, my, mz)])
    air = {(mx, my, mz)}
    while q:
        x, y, z = q.popleft()

        for dx, dy, dz in faceOffsets:
            nx, ny, nz = newPoint = (int(x + dx * 2), int(y + dy * 2), int(z + dz * 2))
            if not (mx <= nx <= Mx and my <= ny <= My and mz <= nz <= Mz):
                continue

            if newPoint in blobPoints or newPoint in air:
                continue

            air.add(newPoint)
            q.append(newPoint)
    return air

def getOutsideSurfaceArea(lns):
    faces, blobPoints, mx, my, mz, Mx, My, Mz = getBlobInfo(lns)
    air = findAirPoints(blobPoints, mx, my, mz, Mx, My, Mz)

    #air faces
    freeFaces = set()
    for x, y, z in air:
        for dx, dy, dz in faceOffsets:
            freeFaces.add((x + dx, y + dy, z + dz))

    #intersection of blob faces and air faces
    return len(set(faces) & freeFaces)

def partA(puz):
    ans = getSurfaceArea(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = getOutsideSurfaceArea(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)