'''
画一个正弦波
'''
import numpy as np
import pdb
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)
pdb.set_trace()

def init():  #这个只是画了一个空的画布
    line.set_data([], [])
    return line,

def animate(i):  #根据i，跟新一整个画布的图像
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=20, interval=20, blit=True)

# anim.save('sine_wave.gif', writer='imagemagick')
plt.show()




###################################################
'''
实时更新的数据图，这个在一些传感器数据的时候用
'''
#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []

    for line in lines:
        x, y = line.split(',') # Delimiter is comma
        xs.append(float(x))
        ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib')

ani = animation.FuncAnimation(fig, animate, interval=1000)
#这里没有定义init之类的函数，
#可以这么理解，fig--准备一个画布，animate--用来修改画布上的内容， interval--隔多久刷新一次，让新的数据出现在画布上面
plt.show()

#####################################################
'''
画柱状图
'''
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)   #一直更新
ax2 = fig.add_subplot(2,1,2)   #固定不更新作为参考

X=[
[2361, 2241, 2641, 2907, 2441, 2839, 3085, 2583, 3220, 3395, 3902],
[1283, 1280, 1503, 1699, 1421, 1737, 1898, 1587, 2014, 2223, 2660],
[3625, 3610, 4217, 4967, 3970, 4928, 5576, 4422, 5752, 6366, 7646],
[1015, 988, 1170, 1345, 1047, 1378, 1559, 1208, 1667, 1816, 2271],
[412, 385, 561, 690, 488, 678, 845, 528, 936, 1066, 1559],
[795, 732, 954, 1202, 861, 1192, 1472, 999, 1547, 1841, 2400],
[370, 374, 480, 582, 427, 627, 748, 471, 761, 932, 1319],
]

size = np.shape(X)
r = [ 1 , size[1]] #更换这两个位置
sta = r[0]
end = r[1] + 1 #左闭右开区间
x1 = np.arange( sta, end )

def animate(i):
    x = x1
    y = X[i]
    ax1.clear()
    # ax1.plot(x,y)
    ax1.bar(x,y)
    ax2.bar(x,X[0], color='b')

ani = animation.FuncAnimation( fig, animate, frames=len(X), interval=200 )
plt.show()

'''
参考
https://zhuanlan.zhihu.com/p/65949658
'''