from puzzle.puzzle_solver import PuzzleSolver
import sys

if __name__ == '__main__':
    chosen_algorithm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    solver = PuzzleSolver(begin_state,[0,1,2,3,4,5,6,7,8], chosen_algorithm, heuristic='manhattan')
    solver.solve()