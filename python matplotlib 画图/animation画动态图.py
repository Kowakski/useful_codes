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
参考
https://zhuanlan.zhihu.com/p/65949658
'''