import utils.distance_metrics as distance_metrics
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