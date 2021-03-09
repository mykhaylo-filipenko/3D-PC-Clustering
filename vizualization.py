import numpy as np

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = []
y = []
z = []
with open("D:/NULP/diploma/room_data/scan003.3d") as file:
    while True:
        new_line = file.readline()
        if not new_line:
            break
        lst = new_line.split()
        x.append(float(lst[0]))
        y.append(float(lst[1]))
        z.append(float(lst[2]))

ax.scatter(x, y, z, c="yellow", s=2, marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

fig = plt.figure()
ax = plt.axes(projection="3d")

plt.show()


