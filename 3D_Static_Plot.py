# import necessary module
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# load data from file
# you can replace this using with open
data1 = np.loadtxt("./pos.txt")
# print (data1)
num=data1.size


datax = data1[:, 0]
datay = data1[:, 1]
dataz = data1[:, 2]

# print (datax)
# print (datay)
# print (dataz)

numx=datax.size
print(numx)
numy=datay.size
print(numy)
numz=dataz.size
print(numz)

# new a figure and set it into 3d
fig = plt.figure()
ax = plt.axes(projection='3d')
# ax = fig.add_subplot(111, projection='3d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read, marker='^', linestyle='-'
ax.plot(datax, datay, dataz, c='r', marker='*', linestyle='--')


plt.show()
