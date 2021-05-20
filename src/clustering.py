import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN, KMeans, Birch, OPTICS, MeanShift, AgglomerativeClustering, SpectralClustering

model = DBSCAN(eps=1.6, min_samples=3)
model.fit_predict(data)
pred = model.fit_predict(data)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=model.labels_, s=1)
ax.view_init(azim=200)
plt.show()

print("number of cluster found: {}".format(len(set(model.labels_))))
print('cluster for each point: ', model.labels_)

for num in range(1, 10):
  X = np.array(data)

  plt.scatter(X[:,0],X[:,1], X[:,2], label='True Position')
  kmeans = KMeans(n_clusters=num)
  kmeans.fit(X)

  fig = plt.figure()
  ax = Axes3D(fig)
  ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=kmeans.labels_, s=1)
  ax.view_init(azim=200)
  plt.show()


brc = Birch(n_clusters=None)
brc.fit(X)
brc.predict(X)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=brc.labels_, s=1)
ax.view_init(azim=200)
plt.show()

X = np.array(
    data
)

clustering = OPTICS(min_samples=3).fit(X)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=clustering.labels_, s=1)
ax.view_init(azim=200)
plt.show()

X = np.array(
  data
)

clustering = SpectralClustering(assign_labels="discretize",
                                random_state=0).fit(X)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=clustering.labels_, s=1)
ax.view_init(azim=200)
plt.show()

X = np.array(
  data
)

clustering = MeanShift(bandwidth=4).fit(X)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=clustering.labels_, s=1)
ax.view_init(azim=200)
plt.show()