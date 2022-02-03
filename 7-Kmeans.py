import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

df = pd.read_csv("7-dataset.csv")
f1 = df['Distance_Feature'].values
f2 = df['Speeding_Feature'].values
X = np.asarray(list(zip(f1, f2)))
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

plt.plot(1)
plt.title('Dataset')
plt.subplot(511)
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.xlabel('distance_feature')
plt.ylabel('speeding_feature')
plt.scatter(f1, f2)

plt.plot(2)
plt.title('K- Means')
plt.subplot(513)
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.xlabel('distance_feature')
plt.ylabel('speeding_feature')
kmeans_model = KMeans(n_clusters=3).fit(X)
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(f1[i], f2[i], color=colors[l], marker=markers[l])

plt.plot(3)
plt.title('EM Algorithm')
plt.subplot(515)
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.xlabel('distance_feature')
plt.ylabel('speeding_feature')
gmm = GaussianMixture(n_components=3).fit(X)
labels = gmm.predict(X)
for i, l in enumerate(labels):
    plt.plot(f1[i], f2[i], color=colors[l], marker=markers[l])

plt.show()
