import queue
import time
import resource
import sys
import math

#### SKELETON CODE ####

## The Class that Represents the Puzzle

class PuzzleState(object):

    """docstring for PuzzleState"""
    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n*n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")

        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []

        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self,DFS=True):
        """expand the node"""
        if len(self.children) == 0:
            if DFS:  #RLDU    
                right_child = self.move_right()
                if right_child is not None:
                    self.children.append(right_child)
                left_child = self.move_left()
                if left_child is not None:
                    self.children.append(left_child)
                down_child = self.move_down()
                if down_child is not None:
                    self.children.append(down_child)
                up_child = self.move_up()
                if up_child is not None:
                    self.children.append(up_child)
            else: #UDLR
                up_child = self.move_up()
                if up_child is not None:
                    self.children.append(up_child)
                down_child = self.move_down()
                if down_child is not None:
                    self.children.append(down_child)
                left_child = self.move_left()
                if left_child is not None:
                    self.children.append(left_child)
                right_child = self.move_right()
                if right_child is not None:
                    self.children.append(right_child)        
        return self.children

# Function that Writes to output.txt
### Students need to change the method to have the corresponding parameters

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

def bfs_search(initial_state):
    """BFS search"""
    frontier = queue.Queue() 
    frontier.put(initial_state)
    frontier_config = {}
    frontier_config[tuple(initial_state.config)] = True
    explored = set()
    nodes_expanded = 0
    max_search_depth = 0

    while not frontier.empty():
        state = frontier.get()
        explored.add(state.config)
        if test_goal(state):
            return (state,nodes_expanded,max_search_depth)
        
        nodes_expanded += 1
        for neighbor in state.expand(DFS=False):
            if neighbor.config not in explored and tuple(neighbor.config) not in frontier_config:   
                frontier.put(neighbor)
                frontier_config[tuple(neighbor.config)] = True
                if neighbor.cost > max_search_depth:
                    max_search_depth = neighbor.cost
    return None

def dfs_search(initial_state):
    """DFS search"""
    frontier = queue.LifoQueue() 
    frontier.put(initial_state)
    frontier_config = {}
    frontier_config[tuple(initial_state.config)] = True
    explored = set()
    nodes_expanded = 0
    max_search_depth = 0

    while not frontier.empty():
        state = frontier.get()
        explored.add(state.config)
        if test_goal(state):
            print("goodjob")
            return (state,nodes_expanded,max_search_depth)
        
        nodes_expanded += 1
        for neighbor in state.expand():
            if neighbor.config not in explored and tuple(neighbor.config) not in frontier_config:   
                frontier.put(neighbor)
                frontier_config[tuple(neighbor.config)] = True
                if neighbor.cost > max_search_depth:
                    max_search_depth = neighbor.cost
    return None

def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    if list(puzzle_state.config) == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True
    else:
        return False

# Main Function that reads in Input and Runs corresponding Algorithm

def main():

    chosen_algorithm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)

    start_time = time.time()
    mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    if chosen_algorithm == "bfs":
        final_states = bfs_search(hard_state)
    elif chosen_algorithm == "dfs":
        final_states = dfs_search(hard_state)
    elif chosen_algorithm == "ast":
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")
    
    mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    running_time = time.time() - start_time
    ram_usage = (mem_final - mem_init) / 1024

    writeOutput(chosen_algorithm, final_states, running_time, ram_usage)

if __name__ == '__main__':

    main()