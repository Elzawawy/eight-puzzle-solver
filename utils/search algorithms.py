import queue

def bfs_search(initial_state):
    """ Search the shallowest nodes in the search tree first."""
    frontier = queue.SimpleQueue(initial_state)
    explored = set()
    while frontier:
        state = frontier.get()
        explored.add(state)
        if state.goal_test(state):
            return state
        for neigbhor in state.expand():
            if neigbhor not in explored and neigbhor not in frontier:
                frontier.put(neigbhor)
    return None

def dfs_search(initial_state):
    """ Search the deepest nodes in the search tree first."""
    frontier = queue.LifoQueue(initial_state)
    explored = set()
    while frontier:
        state = frontier.get()
        explored.add(state)
        if state.goal_test():
            return state
        for neigbhor in state.expand():
            if neigbhor not in explored and neigbhor not in frontier:
                frontier.put(neigbhor)
    return None

    
def a_star_search(initial_state, heuristic):
    """A * search"""
    frontier = queue.PriorityQueue('min', heuristic)
    frontier.put(initial_state)
    explored = set()
    while not frontier.empty:
        state = frontier.get()
        explored.add(state)
        if state.goal_test():
            return state
        for neigbhor in state.expand():
            if neigbhor not in explored and neigbhor not in frontier:
                frontier.put(neigbhor)
            #elif neigbhor in frontier:
