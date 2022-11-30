import re
from aocd.models import Puzzle
from os.path import basename

def getPuzzleObject(file):
    file = basename(file)

    if(re.search('AoC\d\d\d\dd\d',file)):
        y = int(file[3:7])
        file = file[:-3]
        d = int(file[8:])
    else:
        raise Exception('file does not match naming convention: AoC~year~d~day~.py')

    return Puzzle(year = y, day = d)