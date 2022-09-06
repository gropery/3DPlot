import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.widgets import Slider, Button

pTime = 0  # 开始时间初始化
cTime = 0  # 目前时间初始化
wframe = None
pos = 0

########################################################
# 读数据方法1
# data1 = np.loadtxt("./pos.txt")
# datax = data1[:, 0]
# datay = data1[:, 1]
# dataz = data1[:, 2]

# 读数据方法2
lx = []
ly = []
lz = []

fl = open(file="loc_node0", mode='r')
for f1 in fl.readlines():
    # 只取[]中有效数据
    start = f1.find('[')
    end = f1.find(']')
    f2 = f1[start + 1: end].strip()

    # 切分 x,y,z 3轴数据
    pos1 = f2.find(' ')
    pos2 = f2.find(' ', pos1+7)
    str_x = f2[:pos1].strip()
    str_y = f2[pos1+1:pos2].strip()
    str_z = f2[pos2:].strip()

    # 转换 str为float类型
    f_x = float(str_x)
    f_y = float(str_y)
    f_z = float(str_z)

    lx.append(f_x)
    ly.append(f_y)
    lz.append(f_z)

fl.close()

datax = np.array(lx)
datay = np.array(ly)
dataz = np.array(lz)

# 处理数据
numx = datax.size
print(numx)
numy = datay.size
print(numy)
numz = dataz.size
print(numz)

lx1 = []
ly1 = []
lz1 = []

fl = open(file="loc_node1", mode='r')
for f1 in fl.readlines():
    # 只取[]中有效数据
    start = f1.find('[')
    end = f1.find(']')
    f2 = f1[start + 1: end].strip()

    # 切分 x,y,z 3轴数据
    pos1 = f2.find(' ')
    pos2 = f2.find(' ', pos1+7)
    str_x = f2[:pos1].strip()
    str_y = f2[pos1+1:pos2].strip()
    str_z = f2[pos2:].strip()

    # 转换 str为float类型
    f_x = float(str_x)
    f_y = float(str_y)
    f_z = float(str_z)

    lx1.append(f_x)
    ly1.append(f_y)
    lz1.append(f_z)

fl.close()

datax1 = np.array(lx1)
datay1 = np.array(ly1)
dataz1 = np.array(lz1)

# 处理数据
numx1 = datax1.size
print(numx1)
numy1 = datay1.size
print(numy1)
numz1 = dataz1.size
print(numz1)

nummin = min(numx, numx1)
print(nummin)
########################################################
# new a figure and set it into 3d
fig = plt.figure()

# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.25)

# Define initial parameters
init_pos = 0

# Make a horizontal slider to control the frequency.
axpos = plt.axes([0.25, 0.1, 0.65, 0.03])
pos_slider = Slider(
    ax=axpos,
    label='pos point',
    valmin=0,
    valmax=nummin,
    valinit=init_pos,
)


# The function to be called anytime a slider's value changes
def update(val):
    global pos
    pos = int(val)

# register the update function with each slider
pos_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    pos_slider.reset()


button.on_clicked(reset)

########################################################
ax = plt.axes(projection='3d')
# ax = fig.add_subplot(111, projection='3d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# ax.plot(datax, datay, dataz, c='r', marker='*', linestyle='--')
# ax.plot(datax1, datay1, dataz1, c='b', marker='^', linestyle='-')
# plt.show()

while True:
    # If a line collection is already remove it before drawing.
    if wframe:
        plt.cla()  # 清除当前坐标轴

    # Plot the new wireframe and pause briefly before continuing.
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.plot(datax, datay, dataz, c='r', marker='*', linestyle='--')
    ax.plot(datax1, datay1, dataz1, c='b', marker='^', linestyle='-')
    wframe = ax.plot(datax[pos], datay[pos], dataz[pos], c='g', marker='*', linestyle='--')
    ax.plot(datax1[pos], datay1[pos], dataz1[pos], c='y', marker='^', linestyle='-')

    # 更新滑块
    pos_slider.set_val(pos)

    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # print(fps)

    pos += 1
    if pos >= nummin:
        break

    plt.pause(0.01)

