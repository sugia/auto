# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[float('inf') for k in xrange(4)] for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
    prev = {}
    value[init[0]][init[1]][init[2]] = 0
    vec = [tuple(init)]
    while vec:
        x, y, d = vec.pop(0)
        # right turn
        if d == 0:
            xx, yy, dd = x, y+1, (d+3) % 4
        elif d == 1:
            xx, yy, dd = x-1, y, (d+3) % 4
        elif d == 2:
            xx, yy, dd = x, y-1, (d+3) % 4
        elif d == 3:
            xx, yy, dd = x+1, y, (d+3) % 4
        
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]):
            if grid[xx][yy] == 0 and value[xx][yy][dd] > value[x][y][d] + cost[0]:
                value[xx][yy][dd] = value[x][y][d] + cost[0]
                vec.append((xx, yy, dd))
                prev[(xx, yy, dd)] = (x, y, d)
        # no turn
        if d == 0:
            xx, yy, dd = x-1, y, d
        elif d == 1:
            xx, yy, dd = x, y-1, d
        elif d == 2:
            xx, yy, dd = x+1, y, d
        elif d == 3:
            xx, yy, dd = x, y+1, d
            
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]):
            if grid[xx][yy] == 0 and value[xx][yy][dd] > value[x][y][d] + cost[1]:
                value[xx][yy][dd] = value[x][y][d] + cost[1]
                vec.append((xx, yy, dd))
                prev[(xx, yy, dd)] = (x, y, d)
        # left turn
        if d == 0:
            xx, yy, dd = x, y-1, (d+1) % 4
        elif d == 1:
            xx, yy, dd = x+1, y, (d+1) % 4
        elif d == 2:
            xx, yy, dd = x, y+1, (d+1) % 4
        elif d == 3:
            xx, yy, dd = x-1, y, (d+1) % 4
            
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]):
            if grid[xx][yy] == 0 and value[xx][yy][dd] > value[x][y][d] + cost[2]:
                value[xx][yy][dd] = value[x][y][d] + cost[2]
                vec.append((xx, yy, dd))
                prev[(xx, yy, dd)] = (x, y, d)
                
    policy2D = [[' ' for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
    policy2D[goal[0]][goal[1]] = '*'
    
    min_value = min(value[goal[0]][goal[1]])
    state = tuple(init)
    for d in xrange(4):
        if value[goal[0]][goal[1]][d] == min_value:
            state = (goal[0], goal[1], d)
            break
    
    while state in prev:
        prev_state = prev[state]
        # right turn
        if (prev_state[2] + 3) % 4 == state[2]:
            policy2D[prev_state[0]][prev_state[1]] = 'R'
        # no turn
        elif prev_state[2] == state[2]:
            policy2D[prev_state[0]][prev_state[1]] = '#'
        # left turn
        elif (prev_state[2] + 1) % 4 == state[2]:
            policy2D[prev_state[0]][prev_state[1]] = 'L'
        
        state = prev_state
        
    return policy2D
    
'''
policy2D = optimum_policy2D(grid,init,goal,cost)
for row in policy2D:
    print row
'''
