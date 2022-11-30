from aocd.models import Puzzle

def safeSubmit(puzzle: Puzzle, answer: int, part):
    if(input(f'Ready to submit part {part}? [{answer}] (Y/n)\n') == 'Y'):
        if(part == 'a'):
            puzzle.answer_a = answer
        elif(part == 'b'):
            puzzle.answer_b = answer
        else:
            print(f"no part provided with answer {answer}")
    else:
        print('Keep going!')