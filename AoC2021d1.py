import AoCHelpers.setupUtilities.submition as submit
from aocd.models import Puzzle
puz = Puzzle(year=2021, day=1)

submit.safeSubmit(puz, 201, 'a')