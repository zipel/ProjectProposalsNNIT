# Import libraries.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read the input data.
data = np.loadtxt("drivers.txt", delimiter=",")

# K-means clustering.
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)
y_plot = kmeans.fit_predict(data)

# Plot the K-Means clusters.
legend = plt.scatter(data[:, 0], data[:, 1], c=y_plot)
plt.plot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], "r*", markersize=12)
plt.xlabel("Distance Feature")
plt.ylabel("Speeding Feature")
plt.show()