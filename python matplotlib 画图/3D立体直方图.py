# from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import numpy as np

#设置x轴取值
xedges = np.array([10,20,30,40,50,60,70])
#设置y轴取值
yedges = np.array([10,20,30,40,50,60,70])
#设置X,Y对应点的值。即原始数据。
hist =np.array( [[0.0964,0.1024,0.1043,0.1057,0.1072,0.1100],
[0.1027,0.1039,0.1057,0.1069,0.1078,0.1109],
[0.1046,0.1059,0.1061,0.1079,0.1085,0.1114],
[0.1068,0.1079,0.1084,0.1091,0.1096,0.1127],
[0.1091,0.1089,0.1107,0.1112,0.1118,0.1131],
[0.1102,0.1113,0.1121,0.1129,0.1133,0.1157]])

#生成图表对象。
fig = plt.figure()
#生成子图对象，类型为3d
ax = fig.add_subplot(111,projection='3d')

#设置作图点的坐标
xpos, ypos = np.meshgrid(xedges[:-1]-2.5 , yedges[:-1]-2.5 )
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

#设置柱形图大小
dx =5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

#设置坐标轴标签
ax.set_xlabel('R')
ax.set_ylabel('K')
ax.set_zlabel('Recall')

# x, y, z: array - like
# The coordinates of the anchor point of the bars.
# dx, dy, dz: scalar or array - like
# The width, depth, and height of the bars, respectively.
# minx = np.min(x)
# maxx = np.max(x + dx)
# miny = np.min(y)
# maxy = np.max(y + dy)
# minz = np.min(z)
# maxz = np.max(z + dz)
ax.bar3d(xpos, ypos, zpos, dx, dy, dz,color='b',zsort='average')

plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pdb


Z = [ [    0,   314,   178 , 3377 , 1203 ,   55 , 1195 , 3880 , 1616 , 1573 , 2374,  2103, 2634,  3344,    134,     58 ,    0],
 [    0,    56,  1135 , 1596 ,  780 , 1704 , 2094 , 9845 , 4542 , 1685 , 2790,  3955, 1239,  6024,   2234,   2412 ,    0],
 [    0,   770,  2813 , 6426 , 4716 , 2221 , 3126 , 3859 ,   10 , 3455 , 4224,  1157, 1458,  3479,   2684,   9177 ,    0],
 [    0,  2976,  7082 ,10498 , 4267 , 1907 , 7755 , 1879 ,  241 , 3894 , 5637,   545, 2207,  4208,   4051,   9278 ,    0],
 [    0,  8368, 10261 , 8754 ,11280 , 6318 ,11152 , 3009 , 3080 , 2562 , 3676,    99,  371,  5980,   8963,   3826 ,    0],
 [    0,  8732,  4997 ,11124 ,11488 ,   10 ,15455 , 7863 ,11303 , 6436 , 1816,    51, 51  ,4441  , 3845  , 6336   ,  0],
 [    0, 10703,  3762 , 5438 ,   10 , 8276 , 9839 , 4577 , 2278 , 4621 ,   51,    55, 52  ,8844  , 2573  , 4141   ,  0],
 [    0,    10,  3490 , 1181 ,   10 , 5142 , 5215 , 1962 ,  391 ,  940 ,   50,  4183, 811 , 7861 ,  1208 ,  5255  ,   0],
 [    0,    10,  1315 ,   10 ,   10 ,   10 ,   56 , 1860 ,  276 , 1291 ,   51,  2565, 57  ,4198  , 6723  , 6144   ,  0],
 [    0,    10,    10 , 2269 ,   10 ,   10 ,  182 , 1788 ,   10 ,   10 ,   50,    51, 51  ,2749  ,   10  , 4432   ,  0],
 [    0,   189,    10 ,   10 ,  306 ,  227 ,  160 ,   10 ,   10 , 2511 ,   50,    50, 51  ,4260  ,   10  ,   10   ,  0],
 [    0,    57,    50 ,   50 ,   93 ,  295 ,  125 ,  148 ,  184 , 1998 ,   50,    50, 51  ,4417  ,   10  ,   10   ,  0],
 [    0,    82,    84 ,  107 ,  333 ,  397 ,   99 ,   53 ,   50 , 2810 , 1676, 14422, 4288,  4402,    104,   3119 ,    0],
 [    0,    50,    50 ,   50 ,   10 ,   10 ,   10 ,   10 ,   89 , 4586 ,  214,  5572, 2030,  4125,     50,     67 ,    0],
 [    0,    50,    50 ,   50 ,   50 ,   50 ,   60 ,   51 ,   62 , 5073 , 2396,  6382, 1579,  3828,     74,     59 ,    0]]


# 创建 3D 图形对象
fig = plt.figure()
# ax = Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')

# 生成数据
X = np.arange(0, len(Z[0]), 1)
X = X.flatten('F')

Y = np.arange(0, len(Z), 1)
Y = Y.flatten('F')

# pdb.set_trace()
X, Y = np.meshgrid(X, Y)
# Z = np.sqrt(X ** 2 + Y ** 2)
Z = np.array(Z)

# 绘制曲面图，并使用 cmap 着色
ax.plot_surface(X, Y, Z, cmap=plt.cm.winter)
plt.show()
'''