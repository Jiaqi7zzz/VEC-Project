import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/path_new.csv")
path = df.to_numpy()

slope_list = []
path_new_x = []
path_new_y = []
v_ref = []

path_x = path[:,0]
path_y = path[:,1]

n = 4
for i in range(len(path_x) - n + 1):
    total_x = 0
    total_y = 0
    for j in range(i, i + n):
        total_x += path_x[j]
        total_y += path_y[j]    
    slope_list.append((total_y - path_y[i]) / (total_x - path_x[i]))
    if i == 1 or i == 0:
        v_ref.append(30)
        continue

    if slope_list[i - 1] != 0 and abs(slope_list[i] / slope_list[i - 1]) > 1.06: 
        v_ref.append(20)
    else:
        v_ref.append(30)

for i in range(len(path_x) - n + 1 , len(path_x)):
    v_ref.append(30)

def get_dist(a , b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

res = []
res.append(path_x)
res.append(path_y)
res.append(v_ref)

# print(v_ref)
time = []

for i in range(len(v_ref) - 1):
    time.append(get_dist(path[i] , path[i + 1]) / v_ref[i])
time.append(time[-1])
res.append(time)


sum_time = np.cumsum(time)
res.append(sum_time)

res = pd.DataFrame(res).T
res.to_csv("../data/ref_speed.csv" , index=False,header=None)
plt.plot(sum_time,v_ref)
plt.show()