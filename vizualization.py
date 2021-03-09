import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = []
y = []
z = []
with open("D:/NULP/diploma/room_data/scan012.3d") as file:
    i = 0
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

model = DBSCAN(eps=4, min_samples=2)
model.fit_predict(data)
pred = model.fit_predict(data)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=model.labels_, s=1)
ax.view_init(azim=200)
plt.show()

print("number of cluster found: {}".format(len(set(model.labels_))))
print('cluster for each point: ', model.labels_)
