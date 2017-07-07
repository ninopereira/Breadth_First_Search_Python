# ----------
# search() returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, the function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, the function should return the string
# 'fail'
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def get_smallest(open):
  smallest_index = 0;
  smallest_value = open[0][0];
  for i in range(len(open)):
    if open[i][0]<smallest_value:
      smallest_value = open[i][0]
      smallest_index = i
  return smallest_index

def mark_visited(node,visited_grid):
  visited_grid[node[1]][node[2]] = 1
  return visited_grid

def expand_grid(node_to_expand,visited_grid,delta,cost):
  row = node_to_expand[1]
  col = node_to_expand[2]
  new_nodes = []
  for change in delta:

    if (row+change[0])>=0 and (row+change[0])<len(visited_grid):
      if (col+change[1])>=0 and (col+change[1])<len(visited_grid[row+change[0]]):
        if visited_grid[row+change[0]][col+change[1]] == 0:
          new_node = [node_to_expand[0]+cost,row+change[0],col+change[1]]
          new_nodes.append(new_node)
          visited_grid = mark_visited(new_node,visited_grid)
  return [new_nodes,visited_grid]

def check_goal(new_nodes,goal):
  goal_reached = 0
  path = []
  for node in new_nodes:
    if ((node[1] == goal[0]) and (node[2] == goal[1])):
      goal_reached = 1;
      path = node
  return [goal_reached, path]


def search(grid,init,goal,cost):
    visited_grid = list(grid)

    open = []
    open.append([0,init[0],init[1]])
    while (open):
        smallest = get_smallest(open)
        node_to_expand = open[smallest]
        open.remove(node_to_expand)
        visited_grid = mark_visited(node_to_expand,visited_grid)
        [new_nodes,visited_grid] = expand_grid(node_to_expand,visited_grid,delta,cost)
        open = open + new_nodes
        [goal_reached, path] = check_goal(new_nodes,goal)
        if (goal_reached):
          return path
        if len(open)==0:
          break;
    return 'fail'

print (search(grid,init,goal,cost))
