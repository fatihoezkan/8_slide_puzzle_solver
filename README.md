# 8_slide_puzzle_solver
8-slide puzzle using the A⋆-algorithm Heuristic way

The aim of this is to write a program that can solve the well-known 8-slide puzzle using the A⋆-algorithm.

Most of you are probably already familiar with the 8-slide puzzle, since it is a popular as a children’s game.

It consists of a frame in which 8 puzzle pieces can be moved. It is possible to move one of the pieces to the free space (in matris 0 is the blank tile), as long as the piece is horizontally or vertically adjacent to this free square. 
(i.e. the white square swaps with one of the maximum four horizontally or vertically adjacent squares).
Moves to achieve to the goal will be my output.

f(x) = g(x) + h(x)

h(x) -> will be misplaced tiles cost.

g(x) -> I am going to use manhatten distance for more accurate solution, iteration count also can be used. 

min f(x) will be calculated first. 

open_list -> Nodes will be calculated.

closed_list -> Calculated and visited nodes.
