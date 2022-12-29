#Solved on my own, and finished AoC 2022!
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

snafuDigits = ["=", "-", "0", "1", "2"]

def toDecimal(snafu):
    decimal = 0
    currentPower = 0
    for digit in snafu[::-1]:
        decimal += (snafuDigits.index(digit) - 2) * pow(5, currentPower)
        currentPower += 1
    return decimal

def toSnafu(decimal):
    snafu = ""
    endPower = 0

    while(decimal - 1 >= pow(5, endPower + 1) // 2):
        endPower += 1

    for i in range(endPower, -1, -1):
        snafuIndex = int((((decimal + (pow(5, i)/2)) // pow(5, i)) + 2) % 5)
        snafu += snafuDigits[snafuIndex]

    return snafu

def sumInputSnafu(lns):
    total = 0
    for line in lns:
        total += toDecimal(line)
    return toSnafu(total)

def partA(puz):
    ans = sumInputSnafu(lines)
    submit.safeSubmit(puz, ans, 'a')

partA(puz)