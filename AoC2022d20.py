#Not enough time today, so using hyper-neutrino's walkthrough
#Learned and used doubly linked lists
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

puz = getPuzzle.getPuzzleObject(__file__)

class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

def getCircularDoublyLinkedList(lns, decrypt):
    inputList = [Node(int(num) * (811589153 if decrypt else 1)) for num in lns]
    zeroNode = None
    for i in range(len(inputList)):
        inputList[i].right = inputList[(i + 1) % len(inputList)]
        inputList[i].left = inputList[(i - 1) % len(inputList)]

    for k in inputList:
        if k.num == 0:
            zeroNode = k
            break
    return inputList, zeroNode

def mixFile(list):
    numberOfGaps = len(list) - 1
    for k in list:
        p = k
        if k.num > 0:
            for _ in range(k.num % numberOfGaps):
                p = p.right
            if k == p:
                continue
            #remove k from list
            k.right.left = k.left
            k.left.right = k.right
            #insert k after p
            p.right.left = k
            k.right = p.right
            p.right = k
            k.left = p
        else:
            for _ in range(-k.num % numberOfGaps):
                p = p.left
            if k == p:
                continue
            #remove k from list
            k.right.left = k.left
            k.left.right = k.right
            #insert k before p
            p.left.right = k
            k.left = p.left
            p.left = k
            k.right = p
    
    return list

def sumGroveCords(lns, decrypt=False):
    list, zeroNode = getCircularDoublyLinkedList(lns, decrypt)
    
    for _ in range(10 if decrypt else 1):
        list = mixFile(list)

    sum = 0
    for _ in range(3):
        for _ in range(1000):
            zeroNode = zeroNode.right
        sum += zeroNode.num
    return sum

def partA(puz):
    ans = sumGroveCords(lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = sumGroveCords(lines, decrypt=True)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)