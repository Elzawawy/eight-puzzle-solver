import queue
import time
import resource
import sys
import math
import heapq
from utils import distance_metrics

#### SKELETON CODE ####

## The Class that Represents the Puzzle

class PriorityQueue:
    """A Queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first.
    If order is 'min', the item with minimum f(x) is
    returned first; if order is 'max', then it is the item with maximum f(x).
    Also supports dict-like lookup."""

    def __init__(self, order='min', f=lambda x: x):
        self.heap = []

        if order == 'min':
            self.f = f
        elif order == 'max':  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError("order must be either 'min' or 'max'.")

    def append(self, item):
        """Insert item at its correct position."""
        heapq.heappush(self.heap, (self.f(item),item))

    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False

    def extend(self, items):
        """Insert each item in items at its correct position."""
        for item in items:
            self.append(item)

    def pop(self):
        """Pop and return the item (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return heapq.heappop(self.heap)[-1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        """Return current capacity of PriorityQueue."""
        return len(self.heap)

    def __contains__(self, key):
        """Return True if the key is in PriorityQueue."""
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        """Returns the first value associated with key in PriorityQueue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

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
        self.goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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
    frontier = PriorityQueue("min",calculate_total_cost)
    frontier.append(initial_state)
    frontier_config = {}
    frontier_config[tuple(initial_state.config)] = True
    explored = set()
    nodes_expanded = 0
    max_search_depth = 0

    while not frontier.isEmpty():
        state = frontier.pop()
        explored.add(state)
        if test_goal(state):
            return (state,nodes_expanded,max_search_depth)
        
        nodes_expanded += 1
        for neigbhor in state.expand():
            if neigbhor not in explored and tuple(neigbhor.config) not in frontier_config:
                frontier.append(neigbhor)
            elif tuple(neigbhor.config) in frontier_config:
                if calculate_total_cost(neigbhor) < calculate_total_cost(frontier_config[tuple(neigbhor.config)]):
                    frontier.__delitem__(neigbhor)
                    frontier.append(neigbhor)

def calculate_total_cost(state,heuristic='manhattan'):
    """calculate the total estimated cost of a state"""
    sum_heuristic = 0
    for i, item in enumerate(state.config):
        current_row = i // state.n
        current_col = i % state.n
        goal_idx = state.goal.index(item)
        goal_row = goal_idx // state.n
        goal_col = goal_idx % state.n
        if(heuristic == 'manhattan'):
            sum_heuristic += distance_metrics.manhattan_distance(current_row,current_col,goal_row,goal_col)
        elif(heuristic == 'euclidean'):
            sum_heuristic += distance_metrics.eculidean_distance(current_row,current_col,goal_row,goal_col)
        else: 
            raise NotImplementedError("No such Heuristic is supported.")
    return sum_heuristic + state.cost

def calculate_manhattan_dist(current_row,current_col,goal_row,goal_col):
    """calculate the manhattan distance of a tile"""
    return abs(goal_row - current_row) + abs(goal_col - current_col)

def calculate_euclidean_dist(current_row,current_col,goal_row,goal_col):
    """calculate the euclidean distance of a tile"""
    return math.sqrt(pow((goal_row-current_row),2)) + math.sqrt(pow((goal_col-current_col),2))

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    if list(puzzle_state.config) == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True
    else:
        return False

def check_solvability(state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

# Main Function that reads in Input and Runs corresponding Algorithm

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
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")
    
    mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    running_time = time.time() - start_time
    ram_usage = (mem_final - mem_init) / 1024

    writeOutput(chosen_algorithm, final_states, running_time, ram_usage)

if __name__ == '__main__':

    main()