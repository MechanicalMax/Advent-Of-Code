import re
from aocd.models import Puzzle
from os.path import basename

#Return the correct AoC Puzzle object from the calling script's path
def getPuzzleObject(file):
    file = basename(file)
    #Check if the file follows the naming convention (example: AoC2016d8.py)
    if(re.search('AoC\d\d\d\dd\d',file)):
        y = int(file[3:7])
        file = file[:-3]
        d = int(file[8:])
    else:
        raise Exception('file does not match naming convention: AoC~year~d~day~.py')

    return Puzzle(year = y, day = d)