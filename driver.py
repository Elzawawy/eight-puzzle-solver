from puzzle_state import PuzzleState
import sys
import math
from puzzle_solver import check_solvability,calculate_total_cost
from utils.search_algorithms import bfs_search,dfs_search,A_star_search
import time
import resource

def writeOutput(alg,result,running_time,ram_usage):
    """Write Output"""
    f = open('output.txt', mode='w')
    final_state, nodes_expanded, max_search_depth = result
    path_to_goal = [final_state.action]
    cost_of_path = final_state.cost
        
    parent_state = final_state.parent
    while parent_state:
        if parent_state.parent:
            path_to_goal.append(parent_state.action)
        parent_state = parent_state.parent

    path_to_goal.reverse()

    search_depth = len(path_to_goal)
    
    f.write("path_to_goal: " + str(path_to_goal) + "\n")
    f.write("cost_of_path: " + str(cost_of_path) +  "\n")
    f.write("nodes_expanded: " + str(nodes_expanded) + "\n")
    f.write("search_depth: " + str(search_depth) + "\n")
    f.write("max_search_depth: " + str(max_search_depth) +  "\n")
    f.write("running_time: " + str(running_time) + "\n")
    f.write("max_ram_usage: " + str(ram_usage) + "\n")

    f.close()


def main():

    chosen_algorithm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    if(check_solvability(begin_state)== False):
        print("Not Solvable")
        return 
    hard_state = PuzzleState(begin_state, size)

    start_time = time.time()
    mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    if chosen_algorithm == "bfs":
        final_states = bfs_search(hard_state)
    elif chosen_algorithm == "dfs":
        final_states = dfs_search(hard_state)
    elif chosen_algorithm == "ast":
        final_states = A_star_search(hard_state, calculate_total_cost)
    else:
        print("Enter valid command arguments !")
    
    mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    running_time = time.time() - start_time
    ram_usage = (mem_final - mem_init) / 1024

    writeOutput(chosen_algorithm, final_states, running_time, ram_usage)

if __name__ == '__main__':

    main()