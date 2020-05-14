# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
def my_Polygon(x,y):
    '''
    顶点是第一个点坐标为xy，依次逆时针方向
    :param x:
    :param y:
    :return:
    '''
 
    return plt.Polygon([[x, y],
                        [x-1, y-2],
                        [x+1, y-2]], color='g', alpha=0.5) # 0代表全部透明，1不透明
 
def update_points(num):
    '''
    更新数据点，num代表当前帧的帧数，一定为整数，从0开始，FuncAnimation传入一个np.arange(0, 100),就是100帧，
    '''
    pgon1.set_xy([[x[num],x[num]],
                 [x[num]-1,x[num]-2],
                 [x[num]+1,x[num]-2]])
    pgon2.set_xy([[x[num],y[num]],
                  [x[num]-1,y[num]-2],
                  [x[num]+1,y[num]-2]])
    # point_ani.set_y(x[num])
    return pgon1,pgon2,#text_pt, # 返回的对象的内容是下一个帧的数据内容。这里是下一帧的点的位置，和下一帧文本的位置
 
x = np.linspace(-10, 10, 100)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y) # 这个图像曲线不画出来还不好使呢，不能正确呈现动态图。
# 我自己设置的规定顶点逆时针。顺序。
pgon1 = my_Polygon(4,0)
pgon2 = my_Polygon(0,-4)
ax.add_patch(pgon1)
ax.add_patch(pgon2)
 
plt.xlim(xmax=15,xmin=-15)
plt.ylim(ymax=15,ymin=-15)
plt.grid(ls="--")
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=100, blit=True)
 
ani.save('sin_test2.gif', writer='imagemagick', fps=10)
plt.show()