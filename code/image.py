from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_img():
    img = Image.open('../data/map.png')
    gray_image = img.convert('L')
    width , height = gray_image.size
    matrix = [[0 for i in range(width)] for j in range(height)]

    for y in range(height):
        for x in range(width):
            r, g, b , _ = img.getpixel((x, y))
            # if r == 255 and g == 216 and b == 107:
            #     matrix[y][x] = 1
            # if r == 255 and g == 236 and b == 186:
            #     matrix[y][x] = 1
            if r >= 245 and r <= 255 and g >= 245 and g <= 255 and b >= 245 and b <= 255:
                matrix[y][x] = 1
            if r >= 230 and r <= 242 and g >= 235 and g == 246 and b >= 245 and b <= 254:
                matrix[y][x] = 1
            if r >= 210 and r <= 228 and g >= 220 and g <= 234 and b >= 230 and b <= 246:
                matrix[y][x] = 1
    # 217,225,239
    matrix = np.array(matrix)
    return matrix

def max_pooling(matrix):
    # 3*3 stride = 1 的最大池化层
    matrix = matrix[:,:-1]
    height , width = matrix.shape
    new_matrix = [[0 for i in range(width - 2)] for j in range(height - 2)]
    for i in range(0 , height - 2, 1):
        for j in range(0 , width - 2, 1):
            new_matrix[i][j] = max(matrix[i][j] , matrix[i][j+1] , matrix[i][j+2] , matrix[i+1][j] , matrix[i+1][j+1] , matrix[i+1][j+2] , matrix[i+2][j] , matrix[i+2][j+1] , matrix[i+2][j+2])

    return new_matrix

matrix = get_img()
matrix = max_pooling(matrix)
df = pd.DataFrame(matrix)
print(np.array(matrix).shape)
# df.to_csv('../data/map.csv', index=None, header=None)
# plt.imshow(matrix , cmap = 'binary' , interpolation = 'nearest')
# plt.axis("off")
# plt.savefig("../data/binaryMap.png")
# plt.show()