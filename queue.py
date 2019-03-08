import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import time


class Queue:

    def __init__(self, max_length=math.inf, type_check_function=None):
        self.max_length = max_length
        self.data = []

        if type_check_function is None:
            self.type_check_function = lambda item: True
        else:
            self.type_check_function = type_check_function

    def add(self, *items):
        for item in items:
            if not self.type_check_function(item):
                raise ValueError("Item didn't pass specified test: " + str(item))
        self.data += items
        num_to_pop = max(0, len(self.data) - self.max_length)
        self.data = self.data[num_to_pop:]

    def get(self) -> object:
        return self.data

    def __call__(self, *args, **kwargs):
        return self.get()




class Frame_Animator:
    def __init__(self, queue_length):
        self.q_left = Queue(queue_length)
        self.q_right = Queue(queue_length)

    def update(self):
        pullData = open("/home/frank/Downloads/nuitrack_repo/Examples/nuitrack_console_sample/data.txt", "r").read()

        try:
            dataArray = pullData.split('\n')
            x1, y1, z1, x2, y2, z2 = dataArray[0].split()
            self.q_left.add((x1, y1, z1))
            self.q_right.add((x2, y2, z2))

        except:
            print("No body detected")

        print(self.q_right())
        print()
        #self.ax1.plot( *zip(*q_right()), 'bo')
        #self.ax1.set_ylim(0, 1)
        #self.ax1.set_xlim(0, 1)

#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
animate = Frame_Animator(10)
for i in range(1000):
    animate.update()
    time.sleep(1)
#ani = animation.FuncAnimation(fig, animate.update(), interval=1000)
#plt.show()

"""
Define a queue
	specify length
	add values to the end, but keep length

Goal: plot two groups of 3 queues

Animate function
	Pull a line of data from a text file
	Add values to queues
"""



"""import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import math
from math import floor
import time

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlim(-1.0, 1.3)
ax.set_ylim(-1.0, 1.3)
ax.set_zlim(0, 2000)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


with open("data.txt") as file1:
	for line in file1:
		values = line.strip().split()
		#$print(values[0], values[1])
		#plt.plot(round(float(values[0]),3), round(float(values[1]),3), '-o')
		ax.scatter(round(float(values[0]),3), round(float(values[1]),3),round(float(values[2]),3),'-o')
		#plt.pause(.00001) #uncomment for animation


plt.show()

"""