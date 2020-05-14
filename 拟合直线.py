##最小二乘法
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

'''
596, 598, 600, 603, 609, 615, 621
350, 353, 401, 372, 367, 357, 416
596, 1275), (598, 1371), (600, 1400), (603, 1381), (609, 1417), (615, 1470), (621, 1385),

1,     10, 19, 21, 31, 45, 46
2653, 2634, 2670, 2704, 2680, 2634, 2693

     设置样本数据，真实数据需要在这里处理
'''
##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([ 1,     2, 3, 4, 5, 6, 7])
#Yi=np.array([9,18,31,48,69,94])
# (614, 5790), (616, 6055), (618, 5988), (620, 5826), (624, 4715),
Yi=np.array([ 2653, 2634, 2670, 2704, 2680, 2634, 2693])

'''
    设定拟合函数和偏差函数
    函数的形状确定过程：
    1.先画样本图像
    2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
'''

##需要拟合的函数func :指定函数的形状
def func(p,x):
    a,b,c=p
    return a*x*x+b*x+c

##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p,x,y):
    return func(p,x)-y

'''
    主要部分：附带部分说明
    1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
    2.官网的原话（第二个值）：Value of the cost function at the solution
    3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
    4.返回值元组中第一个值的数量跟需要求解的参数的数量一致
'''

#k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0=[10,10,10]

#把error函数中除了p0以外的参数打包到args中(使用要求)
Para=leastsq(error,p0,args=(Xi,Yi))

#读取结果
a,b,c=Para[0]
print("a=",a,"b=",b,"c=",c)
print("cost："+str(Para[1]))
print("求解的拟合直线为:")
print("y="+str(round(a,2))+"x*x+"+str(round(b,2))+"x+"+str(c))

'''
   绘图，看拟合效果.
   matplotlib默认不支持中文，label设置中文的话需要另行设置
   如果报错，改成英文就可以
'''
'''
#画样本点
plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2)

#画拟合直线
# x=np.linspace(0,12,100) ##在0-15直接画100个连续点
x=Xi ##在0-15直接画100个连续点
y=a*x*x+b*x+c ##函数式
plt.plot(x,y,color="red",label="拟合直线",linewidth=2)
plt.legend() #绘制图例
plt.show()
'''