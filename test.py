########################################################
# """
# ==========================
# Rotating 3D wireframe plot
# ==========================
#
# A very simple 'animation' of a 3D plot.  See also rotate_axes3d_demo.
# """

# from __future__ import print_function
#
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
# import time
#
#
# def generate(X, Y, phi):
#     '''
#     Generates Z data for the points in the X, Y meshgrid and parameter phi.
#     '''
#     R = 1 - np.sqrt(X**2 + Y**2)
#     return np.cos(2 * np.pi * X + phi) * R
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Make the X, Y meshgrid.
# xs = np.linspace(-1, 1, 50)
# ys = np.linspace(-1, 1, 50)
# X, Y = np.meshgrid(xs, ys)
#
# # Set the z axis limits so they aren't recalculated each frame.
# ax.set_zlim(-1, 1)
#
# # Begin plotting.
# wframe = None
# tstart = time.time()
# for phi in np.linspace(0, 180. / np.pi, 100):
#     # If a line collection is already remove it before drawing.
#     if wframe:
#         ax.collections.remove(wframe)
#
#     # Plot the new wireframe and pause briefly before continuing.
#     Z = generate(X, Y, phi)
#     wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
#     plt.pause(.01)
#
# print('Average FPS: %f' % (100 / (time.time() - tstart)))


########################################################
# '''
# ==================
# Rotating a 3D plot
# ==================
#
# A very simple animation of a rotating 3D plot.
#
# See wire3d_animation_demo for another simple example of animating a 3D plot.
# '''
#
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # load some test data for demonstration and plot a wireframe
# X, Y, Z = axes3d.get_test_data(0.1)
# ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
#
# # rotate the axes and update
# for angle in range(0, 360):
#     ax.view_init(30, angle)
#     plt.draw()
#     plt.pause(.001)
#

########################################################
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider, Button
#
#
# # The parametrized function to be plotted
# def f(t, amplitude, frequency):
#     return amplitude * np.sin(2 * np.pi * frequency * t)
#
# t = np.linspace(0, 1, 1000)
#
# # Define initial parameters
# init_amplitude = 5
# init_frequency = 3
#
# # Create the figure and the line that we will manipulate
# fig, ax = plt.subplots()
# line, = plt.plot(t, f(t, init_amplitude, init_frequency), lw=2)
# ax.set_xlabel('Time [s]')
#
# # adjust the main plot to make room for the sliders
# plt.subplots_adjust(left=0.25, bottom=0.25)
#
# # Make a horizontal slider to control the frequency.
# axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
# freq_slider = Slider(
#     ax=axfreq,
#     label='Frequency [Hz]',
#     valmin=0.1,
#     valmax=30,
#     valinit=init_frequency,
# )
#
# # Make a vertically oriented slider to control the amplitude
# axamp = plt.axes([0.1, 0.25, 0.0225, 0.63])
# amp_slider = Slider(
#     ax=axamp,
#     label="Amplitude",
#     valmin=0,
#     valmax=10,
#     valinit=init_amplitude,
#     orientation="vertical"
# )
#
#
# # The function to be called anytime a slider's value changes
# def update(val):
#     line.set_ydata(f(t, amp_slider.val, freq_slider.val))
#     fig.canvas.draw_idle()
#
#
# # register the update function with each slider
# freq_slider.on_changed(update)
# amp_slider.on_changed(update)
#
# # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', hovercolor='0.975')
#
#
# def reset(event):
#     freq_slider.reset()
#     amp_slider.reset()
# button.on_clicked(reset)
#
# plt.show()


########################################################
fl = open(file="loc", mode='r')

f1 = fl.readline()
print(f1)

start = f1.find('[')
end = f1.find(']')

f2 = f1[start+1: end]
print(f2)

f3 = f2.strip()
print(f3)

pos1 = f3.find(' ')
pos2 = f3.find(' ', pos1+7)
str_x = f3[:pos1].strip()
str_y = f3[pos1+1:pos2].strip()
str_z = f3[pos2:].strip()
print(type(str_x))
print(str_x)
print(str_y)
print(str_z)

f_x = float(str_x)
f_y = float(str_y)
f_z = float(str_z)
print(type(f_x))
print(f_x)
print(f_y)
print(f_z)

fl.close()
