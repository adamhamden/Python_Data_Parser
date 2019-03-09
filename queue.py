import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

        self.q_left_x = Queue(queue_length)
        self.q_left_y = Queue(queue_length)
        self.q_left_z = Queue(queue_length)

        self.q_right_x = Queue(queue_length)
        self.q_right_y = Queue(queue_length)
        self.q_right_z = Queue(queue_length)

        self.curve_r = None
        self.curve_l = None


    def update(self):
        pullData = open("/home/frank/Downloads/nuitrack_repo/Examples/nuitrack_console_sample/data.txt", "r").read()

        if self.curve_l and self.curve_r is not None:
            self.curve_l.remove()
            self.curve_r.remove()

        try:
            dataArray = pullData.split('\n')
            x1, y1, z1, x2, y2, z2 = dataArray[0].split()

            self.q_left_x.add(float(x1))
            self.q_left_y.add(float(y1))
            self.q_left_z.add(float(z1))

            self.q_right_x.add(float(x2))
            self.q_right_y.add(float(y2))
            self.q_right_z.add(float(z2))

        except:
            print("No body detected")

        self.curve_r = ax.scatter( self.q_right_x() , self.q_right_y() , self.q_right_z(), color = 'C1',marker = 'd')
        self.curve_l = ax.scatter( self.q_left_x() , self.q_left_y() , self.q_left_z(), color = 'C9',marker ='d')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(0, 1.3)
ax.set_ylim(0, 1.3)
ax.set_zlim(0, 2000)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

animate = Frame_Animator(40)

while True:
    animate.update()
    plt.pause(.1)

plt.show()

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