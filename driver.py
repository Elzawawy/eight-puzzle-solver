from puzzle.puzzle_solver import PuzzleSolver
import sys

if __name__ == '__main__':
    chosen_heuristic = None
    chosen_algorithm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    if(chosen_algorithm == 'ast'):
        value = input("Please choose a heuristic fucntion:\n[1] Manhattan Distance  [2] Euclidean Distance  ")
        if(value == str(1)):
            chosen_heuristic = "manhattan"
        elif(value == str(2)):
            chosen_heuristic = "euclidean"
        else: 
            raise Exception("Wrong input heuristic function !") 
        
    solver = PuzzleSolver(begin_state,[0,1,2,3,4,5,6,7,8], chosen_algorithm, heuristic=chosen_heuristic)
    solver.solve()