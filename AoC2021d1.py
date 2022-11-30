import AoCHelpers.setupUtilities.setupUtilities as setup
from aocd.models import Puzzle
puz = Puzzle(year=2021, day=1)

setup.safeSubmit(puz, 201, 'a')