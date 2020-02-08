# 8-PuzzleSolver
<p align = 'center'>Made with :heart: by <b>Amr Elzawawy</b> and <b> Rami Khafagi</b></p>
<p align='center'><img src='https://miro.medium.com/max/924/1*YxeZJzfhW4kn5O5wAGbkIg.gif'/></p>

This work was developed in assignment 1 for *AI Course Fall 2019/2020 offering at AlexU Faculty of Engineering*.

## About 8-Puzzle Game
An instance of the 8-puzzle game consists of a board holding 8 distinct movable
tiles, plusan empty space. For any such board, the empty space may be legally
swapped with any tile horizontally or vertically adjacent to it. In this assignment,
the blank space is going to be represented by the number 0. Given an initial state
of the board, the search problem is to find a sequence of moves that tran-sitions
this state to the goal state; that is, the configuration with all tiles arranged in
ascending order 0,1,2,3,4,5,6,7,8 .

## Implementation Structure
We followed OOP (Object Oriented Paradigm) concepts to construct our code structure. With each object in the list below representing an object in the game world.
- **Puzzle State**: This class represents the puzzle state at a certain time, it includes: configuration,
cost, parent node, children nodes.
- **Puzzle Solver**: It is responsible of solving the input puzzle, and calculating total estimated cost to solve.
- **Search Algorithms**: This module includes the required search algorithms: BFS, DFS and A* written in an abstract way to allow re-use.
- **Distance Metrics**: Again, an abstarct module to allow re-use, it includes the required distance metrics: Euclidean distance and Manhattan distance

- **Priority Queue**: This class has the priority queue data structure used to implement A* search. It is a
wrapper over the standard "heapq" module in Python to add support for delete items.

## Heuistics used
Tried out both **Eculidean** and **Manhattan** distance metrics for heuristics for A* search.
Manhattan distance is found out to be more admissible than Euclidean distance because Euclidean
distance underestimates the cost as it is shorter than Manhattan distance.

## Final Notes
- Intend to implement more search algorithms (e.g. Real Time A* Search) and apply on this work.
- Intend to make a web-based GUI for the game. 

## References
1. *[COS 226 Programming Assignment, at Princeton Univeristy](https://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments/8puzzle.html)*
2. *[Heap queue (or heapq) library in Python ](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)*
