'''
根据灰度图获得最佳的路径
'''
import math
import heapq
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.position == other.position

def gdist(position1, position2):
    dist : float = math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)
    return dist

def astar(start, goal, grid):
    open_list = []
    closed_list = []
    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, start_node)
    # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                #   ,(-1, -1), (-1, 1), (1, -1), (1, 1)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),(-1,-1),(-1,1),(1,-1),(1,1)]

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)
        
        if current_node.position == goal_node.position:
            path = []
            while current_node.parent:
                path.append(current_node.position)
                current_node = current_node.parent
            path.append(start_node.position)
            return path[::-1]

        for direction in directions:
            next_x = current_node.position[0] + direction[0]
            next_y = current_node.position[1] + direction[1]
            next_node = Node((next_x, next_y), current_node)

            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]) or grid[next_x][next_y] == 0:
                continue

            next_node.g = current_node.g + gdist(next_node.position, current_node.position)
            next_node.h = abs(next_x - goal_node.position[0]) + abs(next_y - goal_node.position[1])
            next_node.f = next_node.g + next_node.h

            if next_node in closed_list:
                continue

            if next_node in open_list:
                for node in open_list:
                    if node == next_node and node.f > next_node.f:
                        open_list.remove(node)
                        break

            heapq.heappush(open_list, next_node)

    return None


data = pd.read_excel("../data/map.xlsx" , header = None)
data = data.to_numpy()
# plt.imshow(data , cmap = 'binary' , interpolation = 'nearest')
# plt.axis("off")
# plt.savefig("../data/binaryMap.png")
start = (282,377)
goal = (0,25)

path = astar(start, goal, data)
print(path)

x = [point[0] for point in path]
y = [len(data[0]) - point[1] for point in path]
# f = interp1d(x, y, kind='linear')
# x_interp = np.linspace(min(x), max(x), 100)
# y_interp = f(x_interp)
# plt.plot(x_interp, y_interp)
# plt.show()

plt.plot(y,x)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.gca().xaxis.set_ticklabels([])
plt.gca().yaxis.set_ticklabels([])
plt.scatter(len(data[0]) - start[1],start[0],color = "red" ,s = 200)
plt.scatter(len(data[0]) - goal[1],goal[0],color = "green" , s = 200)
# plt.show()
plt.savefig("../image/path.png")
with open("../data/pathpoint.txt","w") as file:
    for point in path:
        file.write("(" + str(point[0]) + " , " + str(point[1]) + ")" + "\n")
