import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

dividerPackets = [[[2]], [[6]]]

def decodeLine(line, i=0):
    array = []
    num = 0
    while i < len(line):
        curChar = line[i]
        if curChar.isnumeric():
            num *= 10
            num += int(curChar)
        elif curChar == '[':
            innerArray, newIndex = decodeLine(line, i + 1)
            i = newIndex
            array.append(innerArray)
        else:
            if line[i-1].isnumeric():
                array.append(num)
                num = 0
            if curChar == ']':
                return array, i
        i += 1
    return array

def inOrder(left, right):
    listsInOrder = None
    index = 0

    while(listsInOrder == None and index < len(left) and index < len(right)):
        if type(left[index]) == int:
            if type(right[index]) == int:
                if left[index] < right[index]:
                    listsInOrder = 'Correct'
                elif left[index] > right[index]:
                    listsInOrder = 'Wrong'
            else:
                listsInOrder = inOrder([left[index]], right[index])
        else:
            if type(right[index]) == int:
                listsInOrder = inOrder(left[index], [right[index]])
            else:
                listsInOrder = inOrder(left[index], right[index])
        index += 1

    if listsInOrder == None:
        if len(left) < len(right):
            listsInOrder = 'Correct'
        elif len(left) > len(right):
            listsInOrder = 'Wrong'

    return listsInOrder

def sumCorrectOrder(lns):
    numCorrect = 0
    for startIndex in range(0, len(lns) - 1, 3):
        leftData = decodeLine(lns[startIndex])[0]
        rightData = decodeLine(lns[startIndex+1])[0]
        if inOrder(leftData, rightData) == 'Correct':
            numCorrect += int((startIndex / 3) + 1)
    return numCorrect

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if inOrder(array[j], array[j+1]) == "Wrong":
                array[j], array[j+1] = array[j+1], array[j]

def getDecoderKey(lns):
    sortedData = []
    decoderKey = 1

    for startIndex in range(0, len(lns) - 1, 3):
        sortedData.append(decodeLine(lns[startIndex])[0])
        sortedData.append(decodeLine(lns[startIndex+1])[0])

    bubbleSort(sortedData)

    for number, packet in enumerate(dividerPackets):
        index = 2
        while inOrder(sortedData[index-1], packet) == "Correct":
            index += 1
        decoderKey *= index + number

    return decoderKey

def partA(puz):
    ans = sumCorrectOrder(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = getDecoderKey(lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)