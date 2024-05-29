import numpy as np

start_state = np.array([[2, 0, 3], 
                        [1, 6, 4], 
                        [8, 7, 5]])
# print("start state:")
# print(start_state)

# goal state
goal_state = np.array([[1, 2, 3], 
                       [8, 0, 4], 
                       [7, 6, 5]])
# print("goal state:")
# print(goal_state)


def get_neighbours(state):
    neiughbours = []
    empty_field = np.where(state == 0)
    neiughbours.append((empty_field[0][0], empty_field[1][0] - 1))
    neiughbours.append((empty_field[0][0], empty_field[1][0] + 1))
    neiughbours.append((empty_field[0][0] - 1, empty_field[1][0]))
    neiughbours.append((empty_field[0][0] + 1, empty_field[1][0]))
    valid_neighbours = []
    for neighbour in neiughbours:
        if neighbour[0] >= 0 and neighbour[0] <= 2 and neighbour[1] >= 0 and neighbour[1] <= 2:
            valid_neighbours.append(neighbour)
    return valid_neighbours

def find_tile_index(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return (i, j)
            
# print(find_tile_index(start_state, 0))
# print(find_tile_index(goal_state, 0))

def manhatten_distance(state, goal_state):
    distance = 0
    for i in range(9):
        start_index = find_tile_index(state, i)
        goal_index = find_tile_index(goal_state, i)
        difference  = abs(start_index[0] - goal_index[0]) + abs(start_index[1] - goal_index[1])
        distance += difference
    return distance

# print(manhatten_distance(start_state, goal_state))


# lets calculate the h-cost for each state
# h-cost is the number of misplaced tiles
# g cost gonna be manhattan distance

def h_cost(state, goal_state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                cost += 1
    return cost

def f_cost(state, goal_state):  # heurastic a_star calculation
    return h_cost(np.array(state), goal_state) + manhatten_distance(state,goal_state)

# function for swapping the empty field with the neighbour
def swap(old_state, to_swap):
    new_state = old_state.copy()
    empty_field = np.where(new_state == 0)
    empty_field = (empty_field[0][0], empty_field[1][0])
    new_state[empty_field], new_state[to_swap] = new_state[to_swap], new_state[empty_field]
    return new_state

# #try swapping
# print("old state:")
# print(start_state)

# print("new state:")
# new_state = swap(start_state, (1, 1))

# #take it back :)
# start_state = swap(new_state, (0, 1))

# print(start_state)


def a_star(start_state, goal_state):
    path = [start_state] # indexin by iteration

    open_list = [] # new states to be evaluated
    closed_list = [] # alread evaluated states
    
    f = f_cost(start_state, goal_state)
    open_list.append((f, start_state, [start_state]))


    while len(open_list) > 0:
        open_list.sort(key=lambda x: x[0]) # sort based on f score so we can choose best f score
        current_node = open_list.pop(0) # select current node
        closed_list.append(current_node)
        
        if np.array_equal(current_node[1], goal_state):
            return current_node[2]  # return the path its @2
        
        neighbours = get_neighbours(current_node[1]) # find neighbours
        current_path = current_node[2] #the path we have till now
        
        for neighbour in neighbours: #doin swaps and appending new state to path if not visited before
            new_state = swap(current_node[1], neighbour)
            
            if any(np.array_equal(new_state, closed_state[1]) for closed_state in closed_list): # check if the state is already visited and calculated
                continue
            
            path.append(new_state)
            

            f = f_cost(new_state, goal_state) #calculate socre for cur stte
            new_path = current_path + [new_state] # add this state to our path
            open_list.append((f, new_state, new_path))

    return print("couldnt find the path :( ")


# lets run the algorithm
path = a_star(start_state, goal_state)
print("The Path:")
# print(type(path))

for i,j in enumerate(path):
    print("step: ", i)
    print(j)
    print()