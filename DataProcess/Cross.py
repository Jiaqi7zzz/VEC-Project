'''
计算路径的斜率，利用贝塞尔插值防止有过大的拐弯。

detail:
    若该点的斜率与之前偏差角度过大，则对该点之后的n个点进行插值
'''
# from Bezier import bezier
import numpy as np
import matplotlib.pyplot as plt
# import Bezier
import pandas as pd
# path_x = Bezier.path_x
# path_y = Bezier.path_y
# slope = []

def bezier(Ps : np.array , n , t):
    Ps = np.array(Ps)
    if n == 1:
        return Ps[0]
    return (1 - t) * bezier(Ps[0 : n - 1] , n - 1 , t) + t * bezier(Ps[1 : n] , n - 1 , t)


data = pd.read_csv("../data/path_T.csv")
path_x = data.iloc[:,0]
path_y = data.iloc[:,1]
path_x = path_x.to_numpy()
path_y = path_y.to_numpy()
path_all = []
for i in range(len(path_x)):
    path_all.append([int(path_x[i]),int(path_y[i])])


path_new_x = []
path_new_y = []

slope_list = []
n = 4
tabu_list = []
for i in range(len(path_x) - n + 1):
    # selected_points = [i , i + n]
    total_x = 0
    total_y = 0
    for j in range(i, i + n):
        total_x += path_x[j]
        total_y += path_y[j]    
    # print((total_y - path_y[i]) / (total_x - path_x[i]))
    
    # print(total_x , total_y)
    slope_list.append((total_y - path_y[i]) / (total_x - path_x[i]))
    if i == 1 or i == 0:
        continue
    if i in tabu_list:
        continue
    if slope_list[i - 1] != 0 and abs(slope_list[i] / slope_list[i - 1]) > 1.15: 
        
        for t in np.arange(0 , 1 , 0.05):
            # print(path_all[i : i + n] , n , t)
            pos = bezier(path_all[i : i + n], n , t) 
            # 传进去n个点
            path_new_x.append(np.round(pos[0],1))
            path_new_y.append(np.round(pos[1],1))
            # for k in range(i , i + n):
            #     path_x[k] = np.round(pos[0] , 2)
        for idx in range(i , i + n - 1):
            tabu_list.append(idx)
    else:
        path_new_x.append(path_x[i])
        path_new_y.append(path_y[i])

for i in range(len(path_x) - n + 1 , len(path_x)):
    path_new_x.append(path_x[i])
    path_new_y.append(path_y[i])
    
# for i in range(len(path_new_x)):
#     print(path_new_x[i] , path_new_y[i])


path_new = []
path_new.append(path_new_x)
path_new.append(path_new_y)
path_new = pd.DataFrame(path_new)
path_new = path_new.T
path_new.to_csv("../data/path_new.csv" , index = False , header=None)

plt.plot(path_new_x , path_new_y)
# plt.show()
plt.savefig("../image/path_after_cross.png")

# for i in range(len(slope_list)):
#     print(slope_list[i])