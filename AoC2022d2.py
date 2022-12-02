#With this one, I started solving thinking part B would go in
#a different direction. This code is a bit more messy than
#it needs to be, but it got the job done. I guess it is better
#to start simple and refactor for part B later
import AoCHelpers.setupUtilities.submition as submit
import AoCHelpers.setupUtilities.getPuzzleObject as getPuzzle
from aocd import lines

shapePoints = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

roundOutcome = {
    'lost': 0,
    'draw': 3,
    'win': 6
}

puz = getPuzzle.getPuzzleObject(__file__)

def strategyTotal(decode, inputLines):
    total = 0

    for line in inputLines:
        opponentMove, youMove = line.split()
        if(
            (decode['opponent'][opponentMove] == 'Rock' and decode['you'][youMove] == 'Paper')
            or (decode['opponent'][opponentMove] == 'Paper' and decode['you'][youMove] == 'Scissors')
            or (decode['opponent'][opponentMove] == 'Scissors' and decode['you'][youMove] == 'Rock')
        ):
            total += roundOutcome['win']
        elif(decode['opponent'][opponentMove] == decode['you'][youMove]):
            total += roundOutcome['draw']
        else:
            total += roundOutcome['lost']

        total += shapePoints[decode['you'][youMove]]

    return total

def outcomeStrategyTotal(decode, inputLines):
    total = 0
    
    for line in inputLines:
        opponentMove, desiredOutcome = line.split()
        total += roundOutcome[decode['outcome'][desiredOutcome]]
        yourResponse = getResponse(decode['opponent'][opponentMove], decode['outcome'][desiredOutcome])
        total += shapePoints[yourResponse]

    return total

def getResponse(opMove, out):
    if(out == 'win'):
        if (opMove == 'Rock'):
            return 'Paper'
        elif (opMove == 'Scissors'):
            return 'Rock'
        else:
            return 'Scissors'
    elif(out == 'lost'):
        if (opMove == 'Rock'):
            return 'Scissors'
        elif (opMove == 'Scissors'):
            return 'Paper'
        else:
            return 'Rock'
    else:
        return opMove
    
def partA(puz):
    ans = strategyTotal({
        'opponent': {'A':'Rock', 'B':'Paper', 'C':'Scissors'},
        'you': {'X':'Rock', 'Y':'Paper', 'Z':'Scissors'}
    }, lines)
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = outcomeStrategyTotal({
        'opponent': {'A':'Rock', 'B':'Paper', 'C':'Scissors'},
        'outcome': {'X':'lost', 'Y':'draw', 'Z':'win'},
    }, lines)
    submit.safeSubmit(puz, ans, 'b')

partA(puz)
partB(puz)