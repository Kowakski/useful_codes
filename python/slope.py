#线性拟合：y=a+bx
import numpy as np
# 0,0,0,10717,10782, /10728,/ 10434, 10760, 10565,10672,10230,
y_array = np.array([68, 95, 65, 61, 74, 96])
'''
index 6: 4387, 3964, 3267, 2856, 2626, 1657, -516.428589
index 7: 68, 76, 59, 90, 64, 56, -1.857143
index 8: 82, 82, 71, 81, 103, 98, 4.371428
index 11: 68, 95, 65, 61, 74, 96, 2.085714
index 12: 86, 99, 102, 113, 91, 111, 3.200000
index 13: 104, 98, 110, 130, 98, 80, -2.857143
index 16: 2747, 2837, 2828, 2729, 2773, 2622, -26.171429
index 17: 2491, 2527, 2422, 2407, 2227, 2134, -77.142860
index 18: 3573, 3223, 2837, 2574, 2427, 2217, -269.457153
'''
x = [i for i in range(len(y_array))]
x_array = np.array(x)
m = len(x_array) #方程个数

sum_x = np.sum(x_array)
sum_y = np.sum(y_array)
sum_xy = np.sum(x_array * y_array)
sum_xx = np.sum(x_array **2 )
# a=(sum_y*sum_xx-sum_x*sum_xy)/(m*sum_xx-(sum_x)**2)
b=(m*sum_xy-sum_x*sum_y)/(m*sum_xx-(sum_x)**2)
# print("p = {:.4f} + {:.4f}x".format(a,b))
print(b)

