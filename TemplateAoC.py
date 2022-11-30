import AoCHelpers.setupUtilities.submition as submit
from aocd.models import Puzzle
puz = Puzzle(year=2021, day=1)

def partA(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'a')

def partB(puz):
    ans = 0
    submit.safeSubmit(puz, ans, 'b')