import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN, KMeans, Birch, OPTICS, MeanShift, AgglomerativeClustering, SpectralClustering

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = []
y = []
z = []
with open("output.txt") as file:
    i = 0
    while True:
        new_line = file.readline()
        if not new_line:
            break
        lst = new_line.split()
        if len(lst) > 2:
            x.append(float(lst[0]))
            y.append(float(lst[1]))
            z.append(float(lst[2]))

ax.scatter(x, y, z, s=2, marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

fig = plt.figure()
ax = plt.axes(projection="3d")

lst = []

for el in range(len(x)):
    curr_l = [x[el], y[el], z[el]]
    lst.append(curr_l)

data = np.array(
    lst
)

plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], s=1)
ax.view_init(azim=200)
plt.show()