@echo off
Rem gives the window a title
title Open Today's AoC
Rem opens my venv python.exe then runs my AoC setup script with the today flag
"C:\Users\maxsh\OneDrive\Documents\CodingProjects\Advent of Code\Scripts\python.exe" "C:\Users\maxsh\OneDrive\Documents\CodingProjects\Advent of Code\Advent-Of-Code\AoCHelpers\setup.py" --today
Rem closes the file after waiting so the user can see the messages
timeout /t 5