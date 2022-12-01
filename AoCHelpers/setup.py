#Create a new AoC file from a template
from aocd.models import Puzzle
import argparse
import os.path
import datetime
import shutil

#find paths for AoC folders
MAINDIR = os.path.split(os.path.split(__file__)[0])[0]
TEMPLATEDIR = os.path.join(MAINDIR, 'AoCHelpers', 'templateAoCScripts')

#get current day
dateToday = datetime.date.today()

def _createToday():
    #Call new day with today's year and day
    return _newDay(year = dateToday.year, day = dateToday.day)

def _newDay(year=int, day=int):
    #if today is valid
    if (year in range(2015, dateToday.year + 1)):
        if(day in range(1,26)):
            #copy template file and paste to main folder
            targetPath = os.path.join(MAINDIR, f'AoC{year}d{day}.py')

            if(os.path.exists(targetPath)):
                print(f"Path {targetPath} already exists")
            else:
                shutil.copy(os.path.join(TEMPLATEDIR, 'TemplateAoC.py'), targetPath)

            #try to open the new file in vscode
            try:
                os.system(f'code "{targetPath}" -n -a "{os.path.split(MAINDIR)[0]}"')
            except:
                print("Opening new file in vs code failed")

            #return the puzzle object to calling function
            puzzleOfDay = Puzzle(year, day)
            return puzzleOfDay
        else:
            print(f'Invalid day [{day}]')
    else:
        print(f'Invalid year [{year}]')            

def _setupNewDay():
    #Gather argument data
    parser = argparse.ArgumentParser(description='Setup a new AoC day file')
    parser.add_argument('-t', '--today', action='store_true', help='include to attempt to add today\'s AoC file')
    parser.add_argument('-y', '--year', type=int, help='year of AoC file')
    parser.add_argument('-d', '--day', type=int, help='day of AoC file')
    args = parser.parse_args()

    #Call a function to create a new day
    if(args.today):
        return _createToday()
    else:
        return _newDay(year = args.year, day = args.day)

def _setup():
    #Attempt to create a new day and view the puzzle online
    puzzleOfDay = _setupNewDay()
    if(puzzleOfDay):
        puzzleOfDay.view()

if __name__ == "__main__":
    _setup()