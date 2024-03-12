import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd

path = []
with open('../data/pathpoint.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        x, y = map(int, line.strip('()\n').split(','))
        path.append([x,y])


def bezier(Ps,n,t):
    if n == 1:
        return Ps[0]
    return (1 - t) * bezier(Ps[0 : n - 1] , n - 1 , t) + t * bezier(Ps[1 : n] , n - 1 , t)

path_x = []
path_y = []
points = np.arange(0 , len(path) , 10)
for i in tqdm(range(1 , len(points))):
    for t in np.arange(0,1,0.001):
        pos = bezier(np.array(path[points[i - 1] : points[i]]) , len(path[points[i - 1] : points[i]]) , t)
        path_x.append(pos[0])
        path_y.append(pos[1])

data = pd.read_excel("../data/map.xlsx" , header = None)
data = data.to_numpy()
path_y = [len(data[0]) - point for point in path_y]

start = (282,377)
goal = (0,25)
plt.plot(path_y , path_x)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.gca().xaxis.set_ticklabels([])
plt.gca().yaxis.set_ticklabels([])
plt.scatter(len(data[0]) - start[1],start[0],color = "red" ,s = 200)
plt.scatter(len(data[0]) - goal[1],goal[0],color = "green" , s = 200)
# plt.savefig("../image/bezier_path.png")
plt.show()
# with open("../data/bezier_path.txt" , 'w') as file:
#     for i in range(len(path_x)):
#         file.write(f"{np.round(path_x[i],2)} , {np.round(path_y[i],2)}\n")


