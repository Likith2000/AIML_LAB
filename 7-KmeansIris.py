import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

df = pd.read_csv("8-dataset.csv", header=None)
df = df.iloc[:, :-1]
f1 = df.iloc[:, 2]
f2 = df.iloc[:, 3]

colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']
plt.plot(1)
plt.subplot(511)
plt.title("Data")
plt.scatter(f1, f2)

plt.plot(2)
plt.subplot(513)
kmeansMod = KMeans(n_clusters=3).fit(df)
plt.title("K-Means")
for i, l in enumerate(kmeansMod.labels_):
    plt.plot(f1[i], f2[i], color=colors[l], marker=markers[l])

plt.plot(3)
plt.subplot(515)
GM = GaussianMixture(n_components=3).fit(df)
plt.title("EM algo")
plt.xlabel("Petal width")
plt.ylabel("Petal length")
for i, l in enumerate(GM.predict(df)):
    plt.plot(f1[i], f2[i], color=colors[l], marker=markers[l])

plt.show()
